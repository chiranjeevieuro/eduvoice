"""
Google Workspace integration module
"""
from .auth import GoogleAuth
from .services import (
    GoogleClassroomService,
    GoogleCalendarService,
    GoogleSheetsService,
    GoogleDriveService,
    GoogleGmailService
)

__all__ = [
    "GoogleAuth",
    "GoogleClassroomService",
    "GoogleCalendarService",
    "GoogleSheetsService",
    "GoogleDriveService",
    "GoogleGmailService"
]
