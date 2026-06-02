"""
Main entry point for EduVoice AI Assistant
"""
import argparse
import sys
import os
from eduvioce_ai.core import EduVoiceCore
from eduvioce_ai.utils import get_logger

logger = get_logger(__name__)

def main():
    """Main function to run EduVoice AI Assistant"""
    parser = argparse.ArgumentParser(
        description="EduVoice AI Assistant - Voice-First Educational Platform"
    )
    
    parser.add_argument(
        '--user-type',
        choices=['student', 'faculty', 'admin'],
        required=True,
        help='User type: student, faculty, or admin'
    )
    
    parser.add_argument(
        '--mode',
        choices=['voice', 'text'],
        default='text',
        help='Interface mode: voice or text (default: text)'
    )
    
    parser.add_argument(
        '--credentials',
        default='credentials.json',
        help='Path to Google OAuth credentials file (default: credentials.json)'
    )
    
    parser.add_argument(
        '--demo',
        action='store_true',
        help='Run in demo mode without Google services'
    )
    
    args = parser.parse_args()
    
    try:
        logger.info(f"Starting EduVoice AI Assistant - Mode: {args.mode}, User: {args.user_type}")
        
        # Initialize core application
        use_voice = (args.mode == 'voice')
        app = EduVoiceCore(use_voice=use_voice)
        
        # Initialize Google services if not in demo mode
        if not args.demo:
            if os.path.exists(args.credentials):
                app.initialize_google_services(args.credentials)
            else:
                logger.warning(f"Credentials file not found: {args.credentials}")
                logger.info("Running in limited mode without Google services")
        else:
            logger.info("Running in demo mode")
        
        # Setup user
        if not app.setup_user(args.user_type, use_voice=use_voice):
            logger.error("Failed to setup user")
            sys.exit(1)
        
        # Run interactive session
        app.interactive_session()
        
    except KeyboardInterrupt:
        logger.info("Application terminated by user")
        print("\nApplication terminated.")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
