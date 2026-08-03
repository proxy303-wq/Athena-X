from dotenv import load_dotenv
import os

load_dotenv()

TOTP_TOKEN = os.getenv("GROWW_TOTP_TOKEN")
TOTP_SECRET = os.getenv("GROWW_TOTP_SECRET")