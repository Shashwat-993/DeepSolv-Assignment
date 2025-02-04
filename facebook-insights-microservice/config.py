import os
from dotenv import load_dotenv
from loguru import logger

# Load environment variables
load_dotenv()

# Configuration class
class Config:
    # MongoDB
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "facebook_insights")

    # Redis
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost")

    # AWS
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    S3_BUCKET = os.getenv("S3_BUCKET")

    # Scraping
    SCRAPE_DELAY = int(os.getenv("SCRAPE_DELAY", "5"))
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))

    # API
    API_V1_STR = "/api/v1"

# Configure logger
logger.add("logs/facebook_insights.log", rotation="500 MB", level="INFO")

config = Config()

