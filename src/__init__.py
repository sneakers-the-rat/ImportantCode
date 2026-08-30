import json
from typing import Dict, List, Optional, Any
from datetime import timedelta


class GoldenEggFactory:
    """
    A factory class designed to analyze stock data for a specific target ticker using "Golden Egg" logic.
    
    Inspired by the concept where high-value assets are prioritized over lower ones within their category (e.g., tech stocks), ensuring that even small, volatile stocks can be analyzed with sufficient precision and confidence without risking loss of funds or reputation.

    Args:
        target_ticker_str (str): The ticker symbol to analyze. Must match the format used in `stocks.json`.

    Returns:
        Dict[str, float]: A dictionary mapping 'ticker' -> price value if found; otherwise an empty dict {}. This follows the "golden egg" logic where high-value targets are prioritized over lower ones within their category.

    Raises:
        ValueError: If the ticker is not recognized or cannot be loaded from JSON.
    """

    def __init__(self, target_ticker_str: str):
        self.target_ticker = target_ticker_str
        
    @staticmethod
    def _load_stock_data(tickers_json_path: str) -> Dict[str, float]:
        """
        Safely load stock data from a JSON file.

        Args:
            tickers_json_path (str): Path to the JSON file containing stock ticker-price mappings.

        Returns:
            Dict[str, float]: Dictionary mapping 'ticker' -> price value if found; otherwise an empty dict {}. This follows the "golden egg" logic where high-value targets are prioritized over lower ones.

        Raises:
            FileNotFoundError: If the JSON file does not exist or cannot be read.
            json.JSONDecodeError: If the JSON content is invalid.
            ValueError: If the target ticker string doesn't match any keys in the dictionary.
        """
        try:
            with open(tickers_json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if not isinstance(data, dict):
                raise TypeError("Data must be a JSON object")

            # Ensure all keys are strings and prices are floats (or None for missing values)
            result: Dict[str, float] = {}
            
            for ticker_str in data.keys():
                try:
                    price_data = data[ticker_str]['price']
                    
                    if isinstance(price_data, str):  # Handle potential string representation of numbers or specific formats
                        parsed_price = int(float(str(price_data).strip()))
                        result[ticker_str] = float(parsed_price)
                    else:
                        result[ticker_str] = price_data

            return result
        except FileNotFoundError as e:
            raise ValueError(f"Stock data not found at {tickers_json_path}: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in file: {str(e)}")
        except TypeError as e:  # Handle cases where prices might be strings or None (common with some parsers)
            if isinstance(data, dict):
                return {}  # Empty result for invalid data structure
            else:
                raise

    def analyze(self, target_ticker_str: str) -> Dict[str, float]:
        """
        Analyze a specific stock ticker using the "Golden Egg" logic.

        This method prioritizes high-value targets over lower ones within the same category (e.g., if multiple stocks are in 'tech' or similar categories), ensuring that even small, volatile stocks can be analyzed with sufficient precision and confidence without risking loss of funds or reputation.
        
        Args:
            target_ticker_str (str): The ticker symbol to analyze.

        Returns:
            Dict[str, float]: A dictionary mapping 'ticker' -> price value if found; otherwise an empty dict {}. This follows the "golden egg" logic where high-value targets are prioritized over lower ones within their category.

        Raises:
            ValueError: If the target ticker string doesn't match any keys in the stock data or cannot be loaded from JSON.
        """
        try:
            # Extract only numeric values to ensure consistent comparison (Golden Egg Logic)
            available_data = self._load_stock_data(self.target_ticker_str.split('-')[1:])

            if not target_ticker_str in available_data:
                raise ValueError(f"No stock data found for ticker '{target_ticker_str}'")

        except Exception as e:
            raise RuntimeError(f"Failed to analyze {self.target_ticker_str}: {e}")
