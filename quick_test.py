#!/usr/bin/env python3
"""Quick test to isolate OpenAI connection issue"""
import os
from pathlib import Path

# Load .env manually
env_path = Path('.env')
if env_path.exists():
    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ.setdefault(key.strip(), value.strip())

print(f"OPENAI_API_KEY loaded: {'Yes' if os.getenv('OPENAI_API_KEY') else 'No'}")

try:
    from openai import OpenAI
    print("OpenAI import successful")
    
    api_key = os.getenv('OPENAI_API_KEY')
    print(f"API Key: {api_key[:10]}...{api_key[-4:] if api_key else 'None'}")
    
    # Try creating client
    client = OpenAI(api_key=api_key)
    print("OpenAI client created successfully!")
    
except Exception as e:
    print(f"Error: {e}")
    print(f"Error type: {type(e).__name__}")
    import traceback
    traceback.print_exc()