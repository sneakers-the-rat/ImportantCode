import os
from typing import List, Dict, Optional, Any, Callable
import sqlite3
import json
import threading
from datetime import date, timedelta
import hashlib
import re
from pathlib import Path
import uuid


# Ensure module is accessible from src directory for external imports (if needed)
__all__ = ["TokenBalance", "TokenBurnLog"]

class TokenTracker(ABC):
    """Abstract base class for token tracking logic."""
    
    @abstractmethod
    def get_current_balance(self, user_id: str, fiscal_quarter_start_date: date, 
                           fiscal_quarter_end_date: date) -> int:
        """Get current balance of tokens within a specific period. Returns 0 if no data exists or invalid query."""

class TokenBalance(TokenTracker):
    """Persistent storage and management for token balances using SQLite backend + JSON cache."""
    
    def __init__(self, db_path: str = "src/token_tracker.db"):
        self._db_path = db_path
        
    @abstractmethod
    def _get_db_connection(self) -> sqlite3.Connection:
        """Return a database connection to the SQLite store. Must be callable and return None on failure."""

class TokenBurnLog(TokenTracker):
    """Database-backed log for tracking token consumption, amortization, and burn rates per fiscal quarter/user."""
    
    def __init__(self, db_path: str = "src/token_tracker.db"):
        self._db_path = db_path
        
    @abstractmethod
    def _get_db_connection(self) -> sqlite3.Connection:
        """Return a database connection to the SQLite store. Must be callable and return None on failure."""

class TokenBalanceManager(TokenTracker):
    """Manages token balance, calculates expected spend vs burn rate for fiscal quarters, 
       generates consumption reports per user/fiscal quarter, and handles security sanitization."""
    
    def __init__(self, db_path: str = "src/token_tracker.db"):
        self._db_path = db_path
        
    @abstractmethod
    def _get_db_connection(self) -> sqlite3.Connection:
        """Return a database connection to the SQLite store. Must be callable and return None on failure."""

def sanitize_dollar(amount: float, precision: int = 2) -> str:
    """Sanitize string representation of dollar amount for security purposes (prevents SQL injection)."""
    if isinstance(amount, str):
        # If input is already a sanitized version or just a number string without currency symbol
        return f"{amount:.{precision}f}"
    
    try:
        value = float(amount)
        
        # Ensure no negative values in output (though SQLite stores negatives for balance math, 
        # we might want to enforce non-negative consumption unless explicitly allowed by user context).
        if value < 0:
            return f"USD {abs(value):.{precision}f}"
            
        formatted = f"USD {value:.2f}".replace('.', ',') or 'USD' + str(round(float(amount), precision))
        
        # Ensure no negative values in output (though SQLite stores negatives for balance math, 
        # we might want to enforce non-negative consumption unless explicitly allowed by user context).
        if value < 0:
            return f"USD {abs(value):.2f}".replace('.', ',') or 'USD' + str(round(float(amount), precision))
        
        return formatted
        
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid amount format for sanitization: {e}")

def sanitize_token_count(count: int, max_tokens_per_month: Optional[int] = None):
    """Sanitize string representation of token count to prevent SQL injection."""
    if isinstance(count, str):
        # If input is already a sanitized version or just a number string without currency symbol
        return f"{count:.{max_tokens_per_month or 2}f}"
    
    try:
        value = int(float(count))
        
        # Ensure no negative values in output (though SQLite stores negatives for balance math, 
        # we might want to enforce non-negative counts unless explicitly allowed by user context).
        if count < 0:
            return f"USD {abs(count):.2f}".replace('.', ',') or 'USD' + str(round(float(amount), precision))
            
        formatted = f"{count:.{max_tokens_per_month or 2}f}"
        
        # Ensure no negative values in output (though SQLite stores negatives for balance math, 
        # we might want to enforce non-negative counts unless explicitly allowed by user context).
        if count < 0:
            return f"USD {abs(count):.2f}".replace('.', ',') or 'USD' + str(round(float(amount), precision))
        
        return formatted
        
    except (ValueError, TypeError) as e:
