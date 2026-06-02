"""
Core business logic for EduVoice AI Assistant
"""
from eduvioce_ai.utils import get_logger
from eduvioce_ai.interfaces.voice import VoiceInterface, TextInterface
from eduvioce_ai.agents import StudentAgent, FacultyAgent, AdminAgent
from eduvioce_ai.google_workspace import GoogleAuth, GoogleClassroomService, GoogleCalendarService, GoogleSheetsService, GoogleDriveService, GoogleGmailService
from typing import Optional
from enum import Enum

logger = get_logger(__name__)

class UserType(Enum):
    """User types in the system"""
    STUDENT = "student"
    FACULTY = "faculty"
    ADMIN = "admin"


class EduVoiceCore:
    """Core application logic"""
    
    def __init__(self, use_voice: bool = True):
        self.use_voice = use_voice
        self.interface = VoiceInterface() if use_voice else TextInterface()
        self.agent = None
        self.user_type = None
        self.google_services = None
        logger.info(f"EduVoiceCore initialized (use_voice={use_voice})")
    
    def initialize_google_services(self, credentials_file: str = 'credentials.json') -> bool:
        """Initialize Google Workspace services"""
        try:
            auth = GoogleAuth(credentials_file)
            credentials = auth.authenticate()
            
            self.google_services = {
                'classroom': GoogleClassroomService(credentials),
                'calendar': GoogleCalendarService(credentials),
                'sheets': GoogleSheetsService(credentials),
                'drive': GoogleDriveService(credentials),
                'gmail': GoogleGmailService(credentials),
            }
            logger.info("Google Workspace services initialized")
            return True
        except Exception as e:
            logger.error(f"Failed to initialize Google services: {e}")
            return False
    
    def setup_user(self, user_type: str, use_voice: bool = True):
        """Setup user and initialize appropriate agent"""
        try:
            self.user_type = UserType(user_type.lower())
            
            # Reinitialize interface if needed
            if use_voice != self.use_voice:
                self.use_voice = use_voice
                self.interface = VoiceInterface() if use_voice else TextInterface()
            
            # Initialize appropriate agent
            if self.user_type == UserType.STUDENT:
                self.agent = StudentAgent(
                    classroom_service=self.google_services.get('classroom') if self.google_services else None,
                    calendar_service=self.google_services.get('calendar') if self.google_services else None,
                    drive_service=self.google_services.get('drive') if self.google_services else None
                )
                logger.info("Student agent initialized")
            
            elif self.user_type == UserType.FACULTY:
                self.agent = FacultyAgent(
                    classroom_service=self.google_services.get('classroom') if self.google_services else None,
                    calendar_service=self.google_services.get('calendar') if self.google_services else None,
                    gmail_service=self.google_services.get('gmail') if self.google_services else None
                )
                logger.info("Faculty agent initialized")
            
            elif self.user_type == UserType.ADMIN:
                self.agent = AdminAgent(
                    sheets_service=self.google_services.get('sheets') if self.google_services else None,
                    gmail_service=self.google_services.get('gmail') if self.google_services else None
                )
                logger.info("Admin agent initialized")
            
            return True
        except ValueError:
            logger.error(f"Invalid user type: {user_type}")
            return False
        except Exception as e:
            logger.error(f"Error setting up user: {e}")
            return False
    
    def get_user_input(self, prompt: str = "") -> Optional[str]:
        """Get input from user (voice or text)"""
        try:
            if self.use_voice:
                if prompt:
                    self.interface.speak(prompt)
                return self.interface.listen()
            else:
                return self.interface.input_text(prompt)
        except Exception as e:
            logger.error(f"Error getting user input: {e}")
            return None
    
    def provide_response(self, response: str):
        """Provide response to user (voice or text)"""
        try:
            if self.use_voice:
                self.interface.speak(response)
            else:
                self.interface.output_text(response)
        except Exception as e:
            logger.error(f"Error providing response: {e}")
    
    def process_user_request(self, user_input: str) -> str:
        """Process user request through agent"""
        try:
            if not self.agent:
                return "Please set up your user profile first."
            
            response = self.agent.process_input(user_input)
            return response
        except Exception as e:
            logger.error(f"Error processing user request: {e}")
            return "I encountered an error. Please try again."
    
    def interactive_session(self):
        """Run an interactive session"""
        try:
            welcome_message = f"Welcome to EduVoice AI Assistant! I'm here to help {self.user_type.value}s with their educational needs."
            self.provide_response(welcome_message)
            
            while True:
                prompt = "What can I help you with?" if self.use_voice else "\nYour request (type 'exit' to quit): "
                user_input = self.get_user_input(prompt)
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                    goodbye_message = "Goodbye! Have a great day!"
                    self.provide_response(goodbye_message)
                    break
                
                response = self.process_user_request(user_input)
                self.provide_response(response)
        
        except KeyboardInterrupt:
            logger.info("Session interrupted by user")
            self.provide_response("Session ended. Goodbye!")
        except Exception as e:
            logger.error(f"Error in interactive session: {e}")
