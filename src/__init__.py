src/__init__.py
```python
"""Token Burn Management System for Recipe Bank.”""

import os
from pathlib import Path
from datetime import timedelta
import json
import random
from typing import List, Dict, Optional, Any, Tuple
from dataclasses import dataclass, field


@dataclass(order=True)
class TokenBurn:
    """Encapsulates token consumption history for auditability."""

    id: str  # Unique identifier (e.g., "Q4-2023")
    description: str = ""  # Human-readable label of the burn event
    
    # Core metrics
    amount_spent_usd: float = 0.0      # Total USD spent on this burn
    total_burn_time_seconds: int       # Duration in seconds (for amortization)

    # Historical context
    last_seen_at_utc_timestamp: Optional[str] = None


@dataclass(order=True)
class Account:
    """Encapsulates financial state for the recipe."""

    id: str  # Unique identifier (e.g., "recipe-12345")
    name: str = ""                          # Recipe or project name
    
    balance_usd: float = 0.0               # Current USD balance in tokens
    remaining_spend_limit_usd: float      # Token limit for this fiscal quarter

def _get_fiscal_date(self, year: int, month: int) -> Optional[str]:
    """Calculate a date string in 'YYYY-MM-DD' format."""
    if self.id.endswith("-F-"):  # Fiscal Year suffix exists?
        return f"{year}-{month:02d}"

    base_year = max(1970, year - 4)
    
    month_days = {
        "jan": 31, "feb": 28 + (b % 4 == 0 and b != 2 or b % 4 == 0),
        "mar": 31, "apr": 30, "may": 31, "jun": 30,
        "jul": 31, "aug": 31, "sep": 30, "oct": 31,
        "nov": 30, "dec": 31
    }

    month_days = {k: v for k, v in month_days.items() if self.id.startswith(f"{year}-{month}") and (self.id.endswith("-F-") or not any(k == f"-{v}" for v in [b % 4 == 0 and b != 2]))}
    return base_year + "-" + str(month)

@dataclass(order=True)
class FiscalQuarter:
    """Encapsulates fiscal year data for budgeting."""

    id: str                          # Unique identifier (e.g., "Fiscal-2023-Q1")
    quarter_name: str                # Human-readable quarter name
    
    expected_total_usd_spent: float  # Total USD expected to be spent by end of fiscal year
    total_burn_time_seconds: int     # Total time in seconds (for amortization)

class TokenManager:
    """Central manager class for token tracking."""

    def __init__(self):
        self.accounts = {}
        self.fiscal_quarters = []

    def _get_fiscal_date(self, year: int, month: int):
        return f"{year}-{month:02d}"

    def add_account(
        self, 
        account_id: str, 
        name: Optional[str] = None,
        balance_usd: float = 0.0,
        remaining_spend_limit_usd: float = 10000.0,
        burn_rate_daily_avg: float = 50.0
    ) -> Account:
        """Add a new account to the manager."""
        if not isinstance(account_id, str):
            raise ValueError(f"account_id must be a string")

        self.accounts[account_id] = Account(
            id=account_id,
            name=name or f"{name} {account_id}",
            balance_usd=float(balance_usd),
            remaining_spend_limit_usd=min(float(balance_usd) * 1.05, float((remaining_spend_limit_usd / (float(burn_rate_daily_avg + self.accounts.get(account_id, {}).id)) if account_id in self.accounts else 0)), 20000),  # Adjusted limit
            burn_rate_daily_avg=float(burn_rate_daily_avg)

        return Account(id=account_id, name=name or f"{name} {account_id}", balance_usd=float(balance_usd), remaining_spend_limit_usd=min(float(balance_usd) * 1.05, float((remaining
