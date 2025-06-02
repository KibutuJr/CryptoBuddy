import requests
from typing import Dict, Any # Import necessary libraries for HTTP requests and type annotations

class CryptoDataFetcher: # Class to fetch and manage cryptocurrency data
    def __init__(self): 
        self.base_url = "https://api.coingecko.com/api/v3" # Base URL for CoinGecko API
        # Sample data for cryptocurrencies
        self.crypto_db = {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3/10,
            },
            "Solana": {
                "symbol": "SOL",
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "medium",
        "sustainability_score": 5 / 10,

            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6/10,
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10,
            },
            "Polkadot": {
                "symbol": "DOT",
                "price_trend": "falling",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7 / 10,
                }
        }

    def get_crypto_data(self, crypto_id: str) -> Dict[str, Any]: # Method to fetch real-time data for a specific cryptocurrency
        try:
            response = requests.get(f"{self.base_url}/simple/price", 
                                 params={
                                     "ids": crypto_id.lower(), # Convert crypto ID to lowercase for API compatibility
                                     "vs_currencies": "usd", # Fetch price in USD
                                     "include_24hr_change": "true" # Include 24-hour price change
                                 })
            return response.json() 
        except Exception as e:
            print(f"Error fetching data: {e}")
            return {}

    def get_all_crypto_data(self) -> Dict[str, Any]:
        return self.crypto_db  # Fetch data for all cryptocurrencies in the sample database