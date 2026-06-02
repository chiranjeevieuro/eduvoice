"""
EduVoice AI Assistant - Voice-First Educational Platform
A Google Workspace integrated agentic AI application for digital transformation in colleges.
"""

__version__ = "1.0.0"
__author__ = "EduVoice Team"
__description__ = "Voice-first agentic AI assistant for educational institutions"

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
