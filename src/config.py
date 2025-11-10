import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
if not TWITTER_API_KEY:
    raise ValueError("TWITTER_API_KEY not found in env variables")

API_SECRET = os.getenv("API_SECRET")
if not API_SECRET:
    raise ValueError("API_SECRET not found in env variables")

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
if not ACCESS_TOKEN:
    raise ValueError("ACCESS_TOKEN not found in env variables")

ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
if not ACCESS_TOKEN_SECRET:
    raise ValueError("ACCESS_TOKEN_SECRET not found in env variables")

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    raise ValueError("ANTHROPIC_API_KEY not found in env variables")

# POST_INTERVAL_HOURS = int("POST_INTERVAL_HOURS")
# LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")