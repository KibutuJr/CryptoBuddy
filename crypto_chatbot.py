from crypto_analyzer import CryptoAnalyzer
from data_fetcher import CryptoDataFetcher

class CryptoChatbot:
    def __init__(self):
        # Initialize data and analyzer
        fetcher = CryptoDataFetcher()
        self.crypto_data = fetcher.get_all_crypto_data()
        self.analyzer = CryptoAnalyzer(self.crypto_data)
        
        # Bot personality
        self.name = "CryptoBuddy"
        self.greeting = "🤖 Hey there! I'm CryptoBuddy, your AI-powered crypto sidekick! How can I help you today?"
        self.disclaimer = "⚠️ Remember: Crypto is risky—always do your own research!"
    
    def handle_query(self, user_query: str) -> str:
        """Process user input and generate response"""
        query = user_query.lower()
        
        # 1. Sustainability recommendation
        if any(keyword in query for keyword in ["sustainable", "green", "eco"]):
            coin, score_data = self.analyzer.get_most_sustainable()
            
            # If score_data is a dict, pull out the numeric value; otherwise assume it's already numeric
            if isinstance(score_data, dict):
                score = score_data.get("value", 0)
            else:
                score = score_data
            
            return f"🌱 Top sustainable pick: {coin} (Score: {score:.1f}/10)! It's eco-friendly with long-term potential."
        
        # 2. Trending/profitable coins
        elif any(keyword in query for keyword in ["trending", "rising", "profit"]):
            trending_coins = self.analyzer.get_trending_cryptos()
            return f"📈 Currently trending: {', '.join(trending_coins) if trending_coins else 'None found'}"
        
        # 3. Eco-friendly coins
        elif any(keyword in query for keyword in ["eco-friendly", "energy", "efficient"]):
            eco_coins = self.analyzer.get_eco_friendly_cryptos()
            return f"♻️ Eco-friendly coins: {', '.join(eco_coins) if eco_coins else 'None found'}"
        
        # 4. Long-term recommendations
        elif any(keyword in query for keyword in ["long-term", "hold", "investment"]):
            long_term_coins = self.analyzer.get_long_term_recommendations()
            return f"⏳ Best for long-term: {', '.join(long_term_coins) if long_term_coins else 'None found'}"
        
        # 5. Coin-specific analysis
        elif any(keyword in query for keyword in ["tell me about", "analyze", "info on"]):
            for coin in self.crypto_data:
                if coin.lower() in query:
                    analysis = self.analyzer.analyze_crypto(coin)
                    return (
                        f"🔍 {coin} Analysis:\n"
                        f"• Profitability: {analysis['profitability']}\n"
                        f"• Sustainability: {analysis['sustainability']}\n"
                        f"• Energy Efficiency: {analysis['energy_efficiency']}\n"
                        f"• Recommendation: {analysis['recommendation']}"
                    )
            return "❌ Crypto not found. Try 'Bitcoin', 'Ethereum', etc."
        
        # 6. Help/commands with example questions
        elif "help" in query or "what can you do" in query:
            return (
                "💡 I can help with:\n"
                "- Sustainable crypto recommendations (e.g., 'Which cryptocurrency is the most sustainable right now?')\n"
                "- Trending/profitable coins (e.g., 'What are the currently trending cryptos?')\n"
                "- Eco-friendly coins (e.g., 'Show me eco-friendly coins.')\n"
                "- Long-term investment tips (e.g., 'Any long-term investment picks?')\n"
                "- Detailed coin analysis (e.g., 'Analyze Cardano', 'Tell me about Bitcoin', 'Give me info on Solana')\n"
                "\nHere are some example questions to try:\n"
                "1. 'Which cryptocurrency is the most sustainable right now?'\n"
                "2. 'Show me eco-friendly coins.'\n"
                "3. 'What are the currently trending cryptos?'\n"
                "4. 'Any long-term investment picks?'\n"
                "5. 'Analyze Cardano.'\n"
                "6. 'Tell me about Bitcoin.'\n"
                "7. 'Give me info on Solana.'\n"
                "8. 'What’s the best green crypto to buy?'\n"
                "9. 'Help'\n"
                "10. 'What can you do?'"
            )
        
        # Fallback response
        return "🤔 Sorry, I didn't understand. Try asking about sustainability, trends, or specific coins!"

    def start_chat(self):
        """Main chat interaction loop"""
        print(f"\n{self.greeting}\n{self.disclaimer}\n")
        print("Type 'exit' to end the chat\n")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print(f"\n{self.name}: Happy investing! Remember to DYOR! 💰")
                break
                
            response = self.handle_query(user_input)
            print(f"\n{self.name}: {response}\n{self.disclaimer}\n")


# Run the chatbot
if __name__ == "__main__":
    bot = CryptoChatbot()
    bot.start_chat()
