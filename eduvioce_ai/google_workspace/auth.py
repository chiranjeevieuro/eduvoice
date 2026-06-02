"""
Google Workspace Authentication Module
Handles OAuth2 authentication with Google APIs
"""
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.exceptions import DefaultCredentialsError
from eduvioce_ai.utils import get_logger

logger = get_logger(__name__)

SCOPES = [
    'https://www.googleapis.com/auth/classroom.readonly',
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/gmail.send',
]

class GoogleAuth:
    """Handles Google OAuth2 authentication"""
    
    def __init__(self, credentials_file='credentials.json', token_file='token.json'):
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.credentials = None
        
    def authenticate(self):
        """Authenticate with Google API"""
        try:
            # Check if token already exists
            if os.path.exists(self.token_file):
                self.credentials = Credentials.from_authorized_user_file(self.token_file, SCOPES)
                
            # If not authenticated, initiate OAuth flow
            if not self.credentials or not self.credentials.valid:
                if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                    self.credentials.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        self.credentials_file, SCOPES)
                    self.credentials = flow.run_local_server(port=0)
                
                # Save credentials for future use
                with open(self.token_file, 'w') as token:
                    token.write(self.credentials.to_json())
            
            logger.info("Successfully authenticated with Google APIs")
            return self.credentials
            
        except FileNotFoundError:
            logger.error(f"Credentials file not found: {self.credentials_file}")
            raise
        except Exception as e:
            logger.error(f"Authentication error: {e}")
            raise
    
    def get_credentials(self):
        """Get authenticated credentials"""
        if not self.credentials:
            self.authenticate()
        return self.credentials
