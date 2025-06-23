from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

def get_api_key(user_key: str = Security(api_key_header)):
    if user_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return user_key
