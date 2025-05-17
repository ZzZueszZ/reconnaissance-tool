import os
from dotenv import load_dotenv
from .api_keys import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL

load_dotenv()

# Agent Configuration
AGENT_CONFIG = {
    "config_list": [
        {
            "model": "deepseek-coder-33b-instruct",
            "api_key": DEEPSEEK_API_KEY,
            "base_url": DEEPSEEK_BASE_URL
        }
    ],
    "temperature": 0.1,
    "request_timeout": 300,
}

# Output Configuration
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
RAW_DATA_DIR = os.path.join(OUTPUT_DIR, "raw_data")
REPORTS_DIR = os.path.join(OUTPUT_DIR, "reports")

# Create directories if they don't exist
os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)
