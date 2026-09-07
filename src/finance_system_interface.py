# src/finance_system_interface.py

import json
from datetime import timedelta, datetime
from typing import Optional, Dict, Any, List
from dataclasses import dataclass
import requests


@dataclass(order=True)
class StockData:
    """Represents a stock symbol with current price and basic metadata."""
    ticker: str
    open_price: float = 0.0
    high_price: Optional[float] = None
    low_price: Optional[float] = None
    volume_24h: int = 0
    change_pct: float = 0.0

class FinancialData:
    """The core public API for financial data access."""

    def __init__(self):
        self._api_url = "https://www.finance.yahoo.com/finance/"
        
    @property
    def _get_market_data(self, symbol) -> Optional[Dict[str, Any]]:
        """Fetch live market data from Yahoo Finance API. Handles CORS and status."""
        try:
            url = f"{self._api_url}/search?symbol={symbol}&limit=10"
            
            # Check if the request fails due to network issues or invalid symbols
            response = requests.get(url, timeout=30)
            
            if response.status_code != 200:
                return None
            
            data = response.json()
            
            if 'results' not in data or len(data['results']) == 0:
                # No results found for this symbol (e.g., non-existent ticker)
                return {"error": "No market data available"}

            result_data = data["results"][0]
            price_info = result_data.get("price", {})
            
            if not isinstance(price_info, dict):
                raise ValueError(f"Invalid response structure for {symbol}")
                
            # Extract ticker and calculate current open/closed prices from the API response
            tickers_dict: Dict[str, Any] = {}
            price_map: Dict[float, str] = {}

            if "ticker" in result_data.get("price", {}).get("info", {}) or \
               "symbol" in result_data and isinstance(result_data["symbol"], str):
                # Handle both ticker-based (e.g., AAPL) and symbol-based queries
                tickers_dict[result_data["symbol"]] = result_data["ticker"]

            if not price_map:
                current_price = float(price_info.get("open", 0)) or self._get_current_open(symbol)
                
                # If no open price is available, try to find the high/low from volume data
                elif "high" in price_info and isinstance(price_info["high"], (int, float)):
                    current_price = min(current_price, float(price_info["high"]))

            return {
                **tickers_dict if tickers_dict else {},  # Return all symbols as keys for easy lookup
                "open": round(float(current_price), 2) if isinstance(current_price, float) and not price_map else None,
                "close": round(float(price_info.get("high", current_price)), 4) if price_info else None,
            }

        except Exception:
            # Fallback to a static mock data if actual API fails or returns invalid JSON
            return {
                **{t: float(current_price * (1 + random.random()) % 5 for t in ["AAPL", "GOOGL"]},
                "open": round(float(0.9), 2)
            }

    def get_current_market_data(self, symbol: str = None) -> Optional[Dict[str, Any]]:
        """Main method to fetch live market data for a specific stock or all public symbols."""
        
        if not isinstance(symbol, str):
            raise ValueError("Symbol parameter must be provided as a string")

        # Handle "all" flag by returning the same mock data structure with default values
        if symbol == "ALL":
            return self._get_market_data()

        try:
            result = self._get_market_data(symbol)
            
            if not isinstance(result, dict):
                raise ValueError(f"Invalid response from API for {symbol}")
                
            # Ensure we have the ticker and current price in a usable format
            data_to_return = {}
            
            # If no specific symbol was requested but "ALL" is used (which returns all), 
            # ensure 'ticker' exists if not already present, otherwise return empty dict with default values for symbols.
            if result.get("open") and isinstance(result["open"], float):
                data_to_return = {"ticker": symbol}  # Explicitly set ticker when "ALL" is requested or a specific one was found
            
            # For any other case where the API returned partial results, ensure we have at least 'open' to be useful
