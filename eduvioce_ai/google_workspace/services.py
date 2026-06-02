"""
Google Workspace Services Integration
Handles interactions with Classroom, Calendar, Sheets, Drive, and Gmail
"""
from googleapiclient.discovery import build
from eduvioce_ai.utils import get_logger
from typing import List, Dict, Any
from datetime import datetime, timedelta

logger = get_logger(__name__)

class GoogleClassroomService:
    """Google Classroom API service"""
    
    def __init__(self, credentials):
        self.service = build('classroom', 'v1', credentials=credentials)
    
    def get_student_courses(self):
        """Get all courses for the authenticated student"""
        try:
            results = self.service.courses().list(pageSize=10).execute()
            courses = results.get('courses', [])
            logger.info(f"Retrieved {len(courses)} courses")
            return courses
        except Exception as e:
            logger.error(f"Error retrieving courses: {e}")
            return []
    
    def get_course_assignments(self, course_id: str):
        """Get assignments for a specific course"""
        try:
            results = self.service.courses().courseWork().list(
                courseId=course_id,
                pageSize=10
            ).execute()
            assignments = results.get('courseWork', [])
            logger.info(f"Retrieved {len(assignments)} assignments for course {course_id}")
            return assignments
        except Exception as e:
            logger.error(f"Error retrieving assignments: {e}")
            return []
    
    def get_upcoming_assignments(self):
        """Get all upcoming assignments across courses"""
        try:
            courses = self.get_student_courses()
            assignments = []
            for course in courses:
                course_assignments = self.get_course_assignments(course['id'])
                for assignment in course_assignments:
                    assignment['course_name'] = course.get('name', 'Unknown Course')
                    assignments.append(assignment)
            return assignments
        except Exception as e:
            logger.error(f"Error retrieving upcoming assignments: {e}")
            return []


class GoogleCalendarService:
    """Google Calendar API service"""
    
    def __init__(self, credentials):
        self.service = build('calendar', 'v3', credentials=credentials)
    
    def create_event(self, summary: str, start_time: datetime, end_time: datetime = None,
                    description: str = "", attendees: List[str] = None):
        """Create a calendar event"""
        try:
            if end_time is None:
                end_time = start_time + timedelta(hours=1)
            
            event = {
                'summary': summary,
                'description': description,
                'start': {
                    'dateTime': start_time.isoformat(),
                    'timeZone': 'UTC',
                },
                'end': {
                    'dateTime': end_time.isoformat(),
                    'timeZone': 'UTC',
                },
            }
            
            if attendees:
                event['attendees'] = [{'email': email} for email in attendees]
            
            result = self.service.events().insert(calendarId='primary', body=event).execute()
            logger.info(f"Event created: {result.get('id')}")
            return result
        except Exception as e:
            logger.error(f"Error creating event: {e}")
            return None
    
    def get_upcoming_events(self, days: int = 7):
        """Get upcoming events"""
        try:
            now = datetime.utcnow().isoformat() + 'Z'
            end = (datetime.utcnow() + timedelta(days=days)).isoformat() + 'Z'
            
            results = self.service.events().list(
                calendarId='primary',
                timeMin=now,
                timeMax=end,
                maxResults=10,
                singleEvents=True,
                orderBy='startTime'
            ).execute()
            
            events = results.get('items', [])
            logger.info(f"Retrieved {len(events)} upcoming events")
            return events
        except Exception as e:
            logger.error(f"Error retrieving events: {e}")
            return []


class GoogleSheetsService:
    """Google Sheets API service"""
    
    def __init__(self, credentials):
        self.service = build('sheets', 'v4', credentials=credentials)
    
    def get_sheet_data(self, spreadsheet_id: str, range_name: str = "Sheet1"):
        """Read data from a Google Sheet"""
        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id,
                range=range_name
            ).execute()
            
            values = result.get('values', [])
            logger.info(f"Retrieved data from {spreadsheet_id}")
            return values
        except Exception as e:
            logger.error(f"Error reading sheet data: {e}")
            return []
    
    def append_sheet_data(self, spreadsheet_id: str, range_name: str, values: List):
        """Append data to a Google Sheet"""
        try:
            body = {'values': [values]}
            result = self.service.spreadsheets().values().append(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption='USER_ENTERED',
                body=body
            ).execute()
            logger.info(f"Data appended to {spreadsheet_id}")
            return result
        except Exception as e:
            logger.error(f"Error appending sheet data: {e}")
            return None


class GoogleDriveService:
    """Google Drive API service"""
    
    def __init__(self, credentials):
        self.service = build('drive', 'v3', credentials=credentials)
    
    def search_files(self, query: str, max_results: int = 10):
        """Search for files in Google Drive"""
        try:
            results = self.service.files().list(
                q=query,
                spaces='drive',
                pageSize=max_results,
                fields='files(id, name, mimeType, webViewLink)'
            ).execute()
            
            files = results.get('files', [])
            logger.info(f"Found {len(files)} files matching query")
            return files
        except Exception as e:
            logger.error(f"Error searching files: {e}")
            return []
    
    def get_file_content(self, file_id: str):
        """Get file content (for text files)"""
        try:
            file_content = self.service.files().get_media(fileId=file_id).execute()
            logger.info(f"Retrieved content for file {file_id}")
            return file_content
        except Exception as e:
            logger.error(f"Error getting file content: {e}")
            return None


class GoogleGmailService:
    """Google Gmail API service"""
    
    def __init__(self, credentials):
        self.service = build('gmail', 'v1', credentials=credentials)
    
    def send_email(self, to: str, subject: str, body: str):
        """Send an email"""
        try:
            from email.mime.text import MIMEText
            import base64
            
            message = MIMEText(body)
            message['to'] = to
            message['subject'] = subject
            
            raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            result = self.service.users().messages().send(
                userId='me',
                body={'raw': raw_message}
            ).execute()
            logger.info(f"Email sent to {to}")
            return result
        except Exception as e:
            logger.error(f"Error sending email: {e}")
            return None
