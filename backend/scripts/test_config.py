import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from app.ai.config import GEMINI_API_KEY

print("API Key:", GEMINI_API_KEY)