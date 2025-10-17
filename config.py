import os
from dotenv import load_dotenv
from web3 import Web3

# Load .env file (so you can store private keys / API keys safely)
load_dotenv()

# Pull your Alchemy API URL from environment variables
ALCHEMY_HTTP_URL = os.getenv("ALCHEMY_HTTP_URL", "").strip()

# How often to check the blockchain (in seconds)
POLL_SECONDS = int(os.getenv("POLL_SECONDS", "10"))

if not ALCHEMY_HTTP_URL:
    raise RuntimeError("⚠️  You must set ALCHEMY_HTTP_URL in your .env file!")

# Connect to Alchemy using Web3
w3 = Web3(Web3.HTTPProvider(ALCHEMY_HTTP_URL))

if not w3.is_connected():
    raise RuntimeError("❌ Failed to connect to Alchemy — check your API key.")
else:
    print("✅ Connected to Ethereum node!")
