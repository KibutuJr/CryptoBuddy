from typing import Dict, Any, List, Tuple # Import necessary libraries for type annotations - for defining data structures and types

class CryptoAnalyzer: # Class to analyze cryptocurrency data
    def __init__(self, crypto_data: Dict[str, Any]): 
        self.crypto_data = crypto_data

    def get_most_sustainable(self) -> Tuple[str, float]:
        """Find the most sustainable cryptocurrency"""
        return max(
            self.crypto_data.items(),
            key=lambda x: x[1]["sustainability_score"]
        ) 

    def get_trending_cryptos(self) -> List[str]:
        # Find cryptocurrencies with rising price trends 
        return [
            crypto for crypto, data in self.crypto_data.items()
            if data["price_trend"] == "rising"
        ]

    def get_eco_friendly_cryptos(self) -> List[str]:
        # Find cryptocurrencies with low energy use e.g "low" or "medium"
        return [
            crypto for crypto, data in self.crypto_data.items()
            if data["energy_use"] in ["low", "medium"]
        ]

    def get_long_term_recommendations(self) -> List[str]:
        #Get recommendations for long-term investment
        return [
            crypto for crypto, data in self.crypto_data.items()
            if data["sustainability_score"] >= 7/10 and data["price_trend"] == "rising"
        ]

    def analyze_crypto(self, crypto_name: str) -> Dict[str, Any]:
     #Analyze a specific cryptocurrency
        if crypto_name not in self.crypto_data:
            return {"error": "Cryptocurrency not found"}
        
        data = self.crypto_data[crypto_name]
        analysis = {
            "name": crypto_name,
            "profitability": "High" if data["price_trend"] == "rising" and data["market_cap"] == "high" else "Medium",
            "sustainability": "High" if data["sustainability_score"] >= 7/10 else "Medium",
            "energy_efficiency": "High" if data["energy_use"] == "low" else "Medium",
            "recommendation": "Strong Buy" if data["price_trend"] == "rising" and data["sustainability_score"] >= 7/10 else "Consider"
        }
        return analysis 