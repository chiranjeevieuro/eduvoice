"""
Configuration settings for EduVoice AI Assistant
"""
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

# Base paths
BASE_DIR = Path(__file__).parent.parent
PROJECT_ROOT = BASE_DIR.parent

# Application Settings
APP_NAME = os.getenv("APP_NAME", "EduVoice AI Assistant")
APP_DEBUG = os.getenv("APP_DEBUG", "True").lower() == "true"
APP_PORT = int(os.getenv("APP_PORT", 5000))

# Google Cloud Configuration
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI", "http://localhost:5000/auth/callback")

# Voice Configuration
VOICE_LANGUAGE = os.getenv("VOICE_LANGUAGE", "en-US")
VOICE_SPEED = float(os.getenv("VOICE_SPEED", 1.0))
MULTILINGUAL_SUPPORT = os.getenv("MULTILINGUAL_SUPPORT", "True").lower() == "true"
SUPPORTED_LANGUAGES = os.getenv("SUPPORTED_LANGUAGES", "en,te,hi").split(",")

# Agent Configuration
AGENT_MODEL = os.getenv("AGENT_MODEL", "gemini-pro")
AGENT_TEMPERATURE = float(os.getenv("AGENT_TEMPERATURE", 0.7))
ENABLE_AGENTIC_FEATURES = os.getenv("ENABLE_AGENTIC_FEATURES", "True").lower() == "true"

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///eduvioce.db")

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# API Keys
GENAI_API_KEY = os.getenv("GENAI_API_KEY", "")

# Feature Flags
ENABLE_VOICE_INPUT = True
ENABLE_VOICE_OUTPUT = True
ENABLE_MULTILINGUAL = MULTILINGUAL_SUPPORT
ENABLE_CLASSROOM_INTEGRATION = True
ENABLE_CALENDAR_INTEGRATION = True
ENABLE_SHEETS_INTEGRATION = True
ENABLE_DRIVE_INTEGRATION = True

# Supported Languages Mapping
LANGUAGE_CODES = {
    "en": "en-US",
    "te": "te-IN",
    "hi": "hi-IN"
}
