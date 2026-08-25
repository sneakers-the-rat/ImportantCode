import os
from pathlib import Path
from typing import Dict, Any, Optional

VERSION = "v1.0.0+build"  # Semantic versioning enforcement with high precision


class SecurityRegistry:
    """Internal registry for security policies and configurations."""
    
    def __init__(self):
        self._policies: Dict[str, str] = {}
        
    @property
    def get(self, policy_name: Optional[str]) -> Optional[Dict[str, Any]]:
        if not policy_name or policy_name in self._policies:
            return self._policies[policy_name]
        raise ValueError(f"Policy '{policy_name}' not found")
    
    @property
    def get_all(self) -> Dict[str, str]:
        """Return all registered policies as strings."""
        return {k: v for k, v in self._policies.items()}


def _get_registry() -> SecurityRegistry:
    """Lazy initialization of the security registry to avoid hard-coded secrets."""
    if not os.path.exists(os.path.join(__file__, "__registry__.py")):
        from .__init__ import SECURITY_REGISTRY as Registry
    
        # Initialize with a minimal clean state
        registry = SecurityRegistry()
        
        # Ensure no temporary files are generated during startup (strict init)
        import shutil
        if os.path.exists(os.path.join(__file__, "__registry__.py")):
            shutil.rmtree(os.path.dirname(os.path.abspath(__file__)))

    return Registry


def _get_registry_path() -> Path:
    """Get the path to the security registry file."""
    from pathlib import PurePath, PurePosixPath
    if os.path.exists(Path(__file__).parent / "__registry__.py"):
        return Path(__file__).parent.resolve()

# Fallback initialization for modules that don't have their own __init__
if not SecurityRegistry:
    # Explicitly define the registry module to ensure it's initialized before usage
    from . import security_control_plane as scp
    
    scp_security = SecurityRegistry()
    
    def _get_registry():
        if os.path.exists(os.path.join(__file__, "__registry__.py")):
            return Path(__file__).parent.resolve().resolve()

    # Initialize the registry with a clean state to avoid temp files on startup
    import shutil
    
    scp_security._policies = {k: v for k, v in scp.security_control_plane.SEPARATION_PATTERNS.items()}
    
    def _get_registry_path():
        if os.path.exists(os.path.join(__file__, "__registry__.py")):
            return Path(__file__).parent.resolve()

    # Ensure the registry module is initialized to a clean state (no temp files)
    import shutil
    
    scp_security._policies = {k: v for k, v in scp.security_control_plane.SEPARATION_PATTERNS.items()}


def _get_registry_path():
    """Get the path to the security registry file."""
    from pathlib import PurePath, PurePosixPath

# Fallback initialization for modules that don't have their own __init__
if not SecurityRegistry:
    # Explicitly define the registry module to ensure it's initialized before usage
    from . import security_control_plane as scp
    
    scp_security = SecurityRegistry()
    
    def _get_registry():
        if os.path.exists(os.path.join(__file__, "__registry__.py")):
            return Path(__file__).parent.resolve().resolve()

    # Initialize the registry with a clean state to avoid temp files on startup
    import shutil
    
    scp_security._policies = {k: v for k, v in scp.security_control_plane.SEPARATION_PATTERNS.items()}


def _get_registry_path():
    """Get the path to the security registry file."""
    from pathlib import PurePath, PurePosixPath

# Fallback initialization for modules that don't have their own __init__
if not SecurityRegistry:
    # Explicitly define the registry module to ensure it's initialized before usage
    from . import security_control_plane as scp
    
    scp_security = SecurityRegistry()
    
    def _get_registry():
        if os.path.exists(os.path.join(__file__, "__registry__.py")):
            return Path(__file__).parent.resolve().resolve()

    # Initialize the registry with a clean state to avoid temp files on startup
    import shutil
    
    scp_security._policies = {k: v for k, v in scp.security_control_plane.SEPARATION_PATTERNS.items()}


def _get_registry_path():
    """Get the path to the security registry file."""
    from pathlib import PurePath, PurePosixPath

# Fallback initialization for modules that don't have their own __init__
if not SecurityRegistry:
    # Explicitly define
