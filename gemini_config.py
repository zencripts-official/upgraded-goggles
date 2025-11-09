"""Google Gemini 2.0 Flash Configuration

This module contains configuration settings for the Google Gemini 2.0 Flash AI project.
"""

import os
from typing import Dict, Any

# API Configuration
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
GEMINI_MODEL = 'gemini-2.0-flash'
API_ENDPOINT = 'https://generativelanguage.googleapis.com/v1beta'

# Model Parameters
MODEL_CONFIG: Dict[str, Any] = {
    'temperature': 0.7,
    'top_p': 0.95,
    'top_k': 40,
    'max_output_tokens': 8192,
    'candidate_count': 1,
}

# Safety Settings
SAFETY_SETTINGS = [
    {'category': 'HARM_CATEGORY_HARASSMENT', 'threshold': 'BLOCK_MEDIUM_AND_ABOVE'},
    {'category': 'HARM_CATEGORY_HATE_SPEECH', 'threshold': 'BLOCK_MEDIUM_AND_ABOVE'},
    {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'threshold': 'BLOCK_MEDIUM_AND_ABOVE'},
    {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'threshold': 'BLOCK_MEDIUM_AND_ABOVE'},
]

# Application Settings
DEBUG_MODE = os.getenv('DEBUG', 'False').lower() == 'true'
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30

def get_api_config() -> Dict[str, Any]:
    """Returns the complete API configuration."""
    return {
        'api_key': GEMINI_API_KEY,
        'model': GEMINI_MODEL,
        'endpoint': API_ENDPOINT,
        'model_config': MODEL_CONFIG,
        'safety_settings': SAFETY_SETTINGS,
    }

def validate_config() -> bool:
    """Validates that all required configuration is present."""
    if not GEMINI_API_KEY:
        raise ValueError('GEMINI_API_KEY environment variable is not set')
    return True
