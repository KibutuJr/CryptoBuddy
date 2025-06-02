# CryptoBuddy: AI-Powered Cryptocurrency Chatbot

_A Python-based chatbot that provides sustainability, trend, and coin-specific insights on cryptocurrencies._

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Repository Structure](#repository-structure)
4. [Prerequisites](#prerequisites)
5. [Installation & Setup](#installation--setup)
   - [Cloning from GitHub](#cloning-from-github)
   - [Installing Python & Dependencies](#installing-python--dependencies)
   - [Configuring VS Code](#configuring-vs-code)
6. [Running the Chatbot](#running-the-chatbot)
   - [Via Command Line](#via-command-line)
   - [In VS Code (Debug/Run)](#in-vs-code-debugrun)
7. [How to Interact (Example Queries)](#how-to-interact-example-queries)
8. [File Descriptions](#file-descriptions)
9. [Contributing](#contributing)
10. [License](#license)
11. [Contact / Support](#contact--support)

---

## Project Overview

CryptoBuddy is a simple, console-based Python chatbot designed to help users explore various aspects of cryptocurrencies through a clean, conversational interface. It can:

- Recommend the **most sustainable** cryptocurrencies.
- List **trending/rising** coins.
- Show **eco-friendly/energy-efficient** coins.
- Provide **long-term investment** tips.
- Give **coin-specific analysis** (profitability, sustainability, energy-efficiency).

Under the hood, CryptoBuddy relies on:

- **`data_fetcher.py`** – a sample “database” of hard-coded crypto metrics (price trend, market cap, energy use, sustainability scores).
- **`crypto_analyzer.py`** – logic for filtering, scoring, and analyzing coin data.
- **`crypto_chatbot.py`** – the main driver: a loop that takes user queries, passes them to the analyzer, and prints formatted replies.

---

## Features

- 🌱 **Sustainability Recommendation**: Returns the coin with the highest sustainability score.
- 📈 **Trending Coins**: Lists coins whose 24-hour price trend is marked as “rising.”
- ♻️ **Eco-Friendly Coins**: Shows coins with low or medium energy usage.
- ⏳ **Long-Term Recommendations**: Filters for sustainably strong, upward-trending coins.
- 🔍 **Coin-Specific Analysis**: Breaks down profitability, sustainability, energy efficiency, and gives a simple “buy/consider” recommendation.
- ℹ️ **Help Menu**: Shows a list of example questions and supported commands.

---

## Repository Structure

CryptoBuddy/
├── crypto_chatbot.py # Main chatbot interface (entry point)
├── crypto_analyzer.py # Logic for analyzing crypto data
├── data_fetcher.py # Sample “database” and optional real-time fetcher stub
├── README.md # ← You are reading this file
└── requirements.txt # List of external dependencies (e.g., requests)

- **`crypto_chatbot.py`**

  - Contains the `CryptoChatbot` class with `handle_query(...)` and `start_chat()` methods.
  - Detects user keywords, calls the analyzer, and prints responses.

- **`crypto_analyzer.py`**

  - Defines the `CryptoAnalyzer` class.
  - Implements methods like `get_most_sustainable()`, `get_trending_cryptos()`, `get_eco_friendly_cryptos()`, `get_long_term_recommendations()`, and `analyze_crypto(crypto_name)`.

- **`data_fetcher.py`**

  - Contains `CryptoDataFetcher`, which maintains a hard-coded dictionary of sample coins.
  - Includes a stub method (`get_crypto_data(crypto_id)`) for fetching real-time pricing via the CoinGecko API if desired.
  - Primary method `get_all_crypto_data()` returns the local sample database.

- **`requirements.txt`**
  - Lists any Python packages needed (e.g., `requests`).
  - Run `pip install -r requirements.txt` to ensure all dependencies are installed.

---

## Prerequisites

- **Operating System**: Windows, macOS, or Linux (any platform supporting Python 3.8+).
- **Python**: Python 3.13.3 (or 3.8+).
- **Git**: If cloning from GitHub.
- **Visual Studio Code (optional)**: For a richer development/debug experience.

---

## Installation & Setup

### Cloning from GitHub

1. Open a terminal (Command Prompt, PowerShell, or Git Bash).
2. Navigate to the directory where you want to keep the project.
3. Run:

   git clone https://github.com/<your-username>/CryptoBuddy.git
   cd CryptoBuddy

Replace https://github.com/<your-username>/CryptoBuddy.git with your repository URL.

## Installing Python & Dependencies

Ensure Python 3.13.3 is installed

Download the installer from python.org/downloads.

During installation, check “Add Python to PATH”.

## Verify installation in a new terminal:

python --version
Expected output:

Python 3.13.3
Install required packages
In the project’s root folder, run:

pip install -r requirements.txt
requirements.txt should contain at least:

requests>=2.0.0
Configuring VS Code
Open VS Code, then choose File → Open Folder… and select the CryptoBuddy directory.

If the Python extension isn’t installed, open the Extensions tab (Ctrl+Shift+X) and install “Python” (by Microsoft).

Select the Python Interpreter (Ctrl+Shift+P → “Python: Select Interpreter” → choose Python 3.13.3 (×64)).

## (Optional) Create a .vscode/launch.json for debugging:

{
"version": "0.2.0",
"configurations": [
{
"name": "Run CryptoBuddy",
"type": "python",
"request": "launch",
"program": "${workspaceFolder}/crypto_chatbot.py",
"console": "integratedTerminal"
}
]
}

## Install dependencies inside VS Code’s integrated terminal:

pip install -r requirements.txt
Running the Chatbot
Via Command Line
Open a new terminal/PowerShell (make sure Python is on your PATH).

## Navigate to the project folder, for example:

cd C:\Users\PC\OneDrive\Desktop\CryptoBuddy
Run:

python crypto_chatbot.py
You should see:

🤖 Hey there! I'm CryptoBuddy, your AI-powered crypto sidekick! How can I help you today?
⚠️ Remember: Crypto is risky—always do your own research!

Type 'exit' to end the chat

You:
Type any supported query (see Example Queries).

To quit, enter exit or quit.

## In VS Code (Debug/Run)

Open crypto_chatbot.py in the editor.

Press F5 (or go to the Run panel and choose “Run CryptoBuddy” if you created a launch.json).

The integrated terminal will open and start the chatbot loop.

Enter queries just as you would in a normal terminal.

Stop debugging by pressing the Stop button (■) or typing exit in the chat.

## How to Interact (Example Queries)

1. Which cryptocurrency is the most sustainable right now?
2. Show me eco-friendly coins.
3. What are the currently trending cryptos?
4. Any long-term investment picks?
5. Analyze Cardano.
6. Tell me about Bitcoin.
7. Give me info on Solana.
8. What’s the best green crypto to buy?
9. Help
10. What can you do?
    To see these examples again at any time, type help or what can you do.

To analyze a specific coin, include “Analyze” or “Tell me about” followed by the coin’s name exactly as it appears in the data (e.g., “Bitcoin”, “Solana”, “Cardano”, “Polkadot”, “Ethereum”).

File Descriptions
crypto_chatbot.py
Entry point and main chat loop.

CryptoChatbot.handle_query(user_query: str) → str uses keyword matching to route requests to the appropriate analyzer method.

CryptoChatbot.start_chat(): prints greeting/disclaimer and continually prompts the user until they type exit or quit.

crypto_analyzer.py

class CryptoAnalyzer:
def **init**(self, crypto_data: Dict[str, Any]): ...
def get_most_sustainable(self) -> Tuple[str, float]: ...
def get_trending_cryptos(self) -> List[str]: ...
def get_eco_friendly_cryptos(self) -> List[str]: ...
def get_long_term_recommendations(self) -> List[str]: ...
def analyze_crypto(self, crypto_name: str) -> Dict[str, Any]: ...
Takes the dictionary from data_fetcher.py and filters or ranks coins based on fields like sustainability_score, price_trend, energy_use, and market_cap.

data_fetcher.py

import requests

class CryptoDataFetcher:
def **init**(self):
self.base_url = "https://api.coingecko.com/api/v3"
self.crypto_db = { # Sample data for Bitcoin, Solana, Ethereum, Cardano, Polkadot
}

    def get_crypto_data(self, crypto_id: str) -> Dict[str, Any]: ...
    def get_all_crypto_data(self) -> Dict[str, Any]: ...

Contains a sample in-memory “database.”

Stub method get_crypto_data() shows how you could fetch real pricing data from CoinGecko if you expand this project.

requests>=2.0.0
Specifies that the requests library is required for any real-time API calls (even though the sample data is hard-coded).

## Contributing

Contributions are welcome! To propose changes or improvements:

## Fork this repository.

## Create a new branch:

git checkout -b feature/your-feature-name

## Make your changes and commit:

git commit -m "Add feature XYZ"

## Push your branch:

git push origin feature/your-feature-name
Open a Pull Request on GitHub. Describe what you changed and why.

After review, your PR can be merged into main.

Please ensure any new code is PEP 8-compliant and includes docstrings or comments for clarity.

License
This project is released under the MIT License. Feel free to copy, modify, and distribute under the terms of MIT.

Authors:

## Thank you for using CryptoBuddy!

Remember: Crypto markets are volatile. Always do your own research (DYOR).
