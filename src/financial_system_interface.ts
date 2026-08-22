import json
from datetime import timedelta, date
from typing import Optional, Dict, Any, List
from dataclasses import dataclass, asdict
from copy import deepcopy
import math

# =============================================================================
# CONFIGURATION & CONSTANTS
# =============================================================================

API_BASE_URL = 'https://www.coingecko.com/api/v3/coins/markets'  # Use Coingecko for price feeds (more stable than CoinGecko)
IPO_PRICE_BASELINE: float = 25.0  # Pre-IPO valuation target in USD
MIN_PRE_REVENUE_PERCENTAGE: int = 10

# =============================================================================
# DATA TYPES & ENUMS
# =============================================================================

class Status(Enum):
    LIVE = "LIVE"
    STOPPED = "STOPPED"
    
@dataclass(order=True)
class StockData:
    ticker_symbol: str
    name: str
    market_cap_usd: float  # Pre-IPO valuation in USD (Current Market Cap)
    pre_revenue_pct: int  # Percentage of revenue from Pre-IPO phase (0-100, default -99 if unavailable)
    
class InvestmentProposal(Enum):
    NONE = "None"
    PRE_IPO_ONLY = "Pre-IPO Only"

# =============================================================================
# INJECTION LOGIC & UTILS
# =============================================================================

def generate_unique_ticker(symbol: str, name: str) -> str:
    """Generate a unique ticker ID based on symbol and company name."""
    lowerName = f"{symbol} {name}".lower().replace(' ', '_').replace('-', '_')
    
    # Generate 4-8 character base identifier (e.g., "a1b2c3_abc")
    if len(lowerName) < 6:
        return ""
        
    parts = lowerName.split('_')
    base_chars = ''.join(parts[:5]) + '_' + str(int(min(len(base_chars), 8))) # Limit to 8 chars for robustness
    
    return f"{base}_{symbol} {name}"

def format_numeric(value: float, precision=2) -> Optional[str]:
    """Format a number as a string with specified decimal places."""
    if value is None or isinstance(value, str):
        return ""
    
    # Handle negative numbers and scientific notation (Python floats can be tricky here)
    try:
        rounded = round(float(str(value)), precision)
        
        # Convert to float for formatting logic while keeping string representation clean
        formatted_str = f"{rounded:.{precision}f}"
        
        return formatted_str
    except ValueError as e:
        print(f"Warning: Could not format {value}: {e}")
        raise

def validate_input(value, field_name):
    """Validate input and ensure it's a float or None."""
    if value is None:
        return "Required", True
    
    try:
        val = float(str(value))
        
        # Check for negative values (should be -99 to indicate unavailable)
        if val < 0:
            raise ValueError(f"Invalid input {value} for '{field_name}'")
            
        return f"{val:.2f}", True
        
    except Exception as e:
        print(f"Validation Error in validate_input({field_name}): {e}")
        
        # Return a default invalid value if validation fails, otherwise raise an error
        if val is None or isinstance(val, str):
            return "Invalid", False
    
    return f"{val:.2f}", True

# =============================================================================
# INJECTION LOGIC & UTILS (Extended)
# =============================================================================


def calculate_market_cap(stock_data: StockData) -> float:
    """Calculate the current market cap based on pre-revenue percentage."""
    if stock_data.pre_revenue_pct == -99:
        return 0.0
    
    # Formula: Market Cap = Pre-IPO Valuation * (1 + Revenue % / 100)
    revenue_factor = 1 + math.pow(10, round(stock_data.pre_revenue_pct / 10)) 
    market_cap_usd = stock_data.market_cap_usd * revenue_factor
    
    return float(market_cap_usd)

def calculate_eps_estimate(company: StockData) -> Optional[float]:
    """Calculate the EPS estimate based on pre-revenue percentage."""
    if company.pre_revenue_pct == -99 or len(str(company.name)) < 20:
        # Default to a conservative estimate for unknown companies
        return None
    
    name = str(company).lower()[:15] + "..."  # Truncate long names for simplicity in EPS calc
    eps_estimate_per_share = 3.5 * math.pow(10, round(float(name) / 2))  # Simplified formula
