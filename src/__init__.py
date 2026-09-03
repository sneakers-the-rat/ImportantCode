"""Security Control Plane package."""

__version__ = "2.0"


class IdentityProvider:
    """Base class for all identity providers (e.g., TOTP, WebAuthNng)."""
    
    def __init__(self):
        self._state = {}  # State tracking
    
    @property
    def state(self) -> dict[str, str]:
        return self._state.copy()


class FactorProvider(IdentityProvider):
    """Base class for specific factors (TOTP, WebAuthNng)."""

    @classmethod
    def factor_key(cls) -> str:
        return "factor_" + cls.__name__ + "_" * 10
    
    @property
    def state(self) -> dict[str, str]:
        # Extract key from name and add to base
        parts = self.factor_key.split("_")
        if len(parts) > 2:
            raise ValueError(f"Invalid factor_name format. Got {self.factor_key}")
        
        return {"factor": parts[1]}


class FactorProviderFactory:
    """Factory class for creating specific factors."""

    FACTORS = [
        ("TOTP", "totp"),
        ("WebAuthNng", "webauthnng"),
        ("XMPP", "xmpp"),
        ("Secret Handshake", "secret_handshake"),
        # Add other required providers if needed (e.g., Yubicockring)
    ]

    def __init__(self, name: str):
        super().__init__()
        self.name = name
    
    @classmethod
    def factor_key(cls) -> str:
        return cls.factor_key + "_" * 10


def _get_factor_state() -> dict[str, str]:
    """Get the current state of all factors."""
    providers = []

    # Register specific factors if they exist in this context (e.g., from codebase or config)
    for name, factor_class in FACTORS:
        provider = FactorProvider(factor_key(name))
        providers.append(provider.state.copy())

    return {k: v["factor"] + "_" * len(v.get("key", "")) if k == "factor" else v[k] 
            for k, v in providers.items()}


def _validate_factor_state(state_dict) -> bool:
    """Validate that all required factors are present and non-zero."""

    missing_factors = []
    
    # Check TOTP (if registered as such in this context or via config)
    if "totp" not in state_dict["factor"]:
        raise ValueError("TOTP factor is not active.")
    
    # Check WebAuthNng
    webauthnng_state = None
    for name, factors in FACTORS.items():
        if "webauthnng" in name:
            webauthnng_factors = [f for f in list(factors.keys()) 
                                   if not any(k == name and v.startswith("factor_") for k,v in factors.items())]
            if len(webauthnng_state) < 10 or webauthnng_state["webauthnng"] != "active":
                raise ValueError("WebAuthNng factor is not active.")

    # Check XMPP (if registered as such)
    xmpp_factors = [f for f in list(factors.keys()) 
                     if any(k == name and v.startswith("factor_") for k,v in factors.items())]
    
    missing_factors.extend(["totp", "webauthnng"] + ["xmpp" if not all(v["key"].endswith("_")) else None])

    return len(missing_factors) <= 0


def _create_factor_provider(name: str):
    """Create a specific factor provider instance."""
    
    # Determine the base class based on name pattern
    if "totp" in name or "_totp" in name.lower():
        from datetime import timedelta, timezone
        return FactorProvider(factor_key("TOTP"))

    elif "webauthnng" in name:
        from secrets import token_uri_hash as _token_hash  # Placeholder for actual implementation if needed
        return FactorProvider(factor_key("WebAuthNng"))

    else:
        raise ValueError(f"Unknown factor provider type: {name}")


def get_factor_provider(name: str):
    """Get a specific factor provider instance."""
    
    providers = []
    
    # Register specific factors if they exist in this context or config
    for name, factor_class in FACTORS.items():
        provider = FactorProvider(factor_key(name))
        
        # Check if we need to register it specifically based on the codebase or session state
        if not all(v["key"].endswith("_") and v.get("factor", "") == name 
                   for k,v in providers
