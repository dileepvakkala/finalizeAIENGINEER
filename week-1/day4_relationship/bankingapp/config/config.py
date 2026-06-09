from dotenv import load_dotenv
import os
import logging
load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)
logging.basicConfig(
    level= logging.INFO)
logger= logging.getLogger("Config")
logger.info("Loaded DATABASE_URL from environment variables: "+str(DATABASE_URL))
SECRET_KEY = os.getenv(
    "SECRET_KEY"
)
