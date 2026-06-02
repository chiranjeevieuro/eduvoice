"""
Agentic AI Engine Module
Implements agentic AI using LangChain and Google Generative AI
"""
from langchain_core.tools import tool
from langchain import agents
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from eduvioce_ai.utils import get_logger
from config.settings import AGENT_MODEL, AGENT_TEMPERATURE, GENAI_API_KEY
from typing import Dict, List, Any
import json

logger = get_logger(__name__)

class EduVoiceAgent:
    """Main agentic AI agent for EduVoice"""
    
    def __init__(self):
        try:
            self.llm = ChatGoogleGenerativeAI(
                model=AGENT_MODEL,
                temperature=AGENT_TEMPERATURE,
                google_api_key=GENAI_API_KEY
            )
            self.memory = ConversationBufferMemory(memory_key="chat_history")
            self.tools = []
            self.agent = None
            self.agent_executor = None
            logger.info("EduVoiceAgent initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing EduVoiceAgent: {e}")
            raise
    
    def add_tool(self, tool_func, description: str):
        """Add a tool to the agent"""
        self.tools.append({
            'func': tool_func,
            'description': description
        })
        logger.info(f"Tool added: {tool_func.__name__ if hasattr(tool_func, '__name__') else 'tool'}")
    
    def initialize_agent(self):
        """Initialize the agent with tools"""
        try:
            # Simplified agent execution without tools for now
            logger.info("Agent initialized")
        except Exception as e:
            logger.error(f"Error initializing agent: {e}")
            raise
    
    def process_input(self, user_input: str) -> str:
        """Process user input and generate response"""
        try:
            if not self.agent:
                self.initialize_agent()
            
            logger.info(f"Processing input: {user_input}")
            # Use the LLM directly for responses
            from langchain_core.messages import HumanMessage
            messages = [HumanMessage(content=user_input)]
            response = self.llm.invoke(messages)
            logger.info(f"Generated response: {response.content}")
            return response.content
        except Exception as e:
            logger.error(f"Error processing input: {e}")
            return "I encountered an error processing your request. Please try again."
    
    def get_conversation_history(self) -> List[Dict]:
        """Get conversation history"""
        return self.memory.load_memory_variables({}) if self.memory else []


class StudentAgent(EduVoiceAgent):
    """Agent specialized for student interactions"""
    
    def __init__(self, classroom_service=None, calendar_service=None, drive_service=None):
        super().__init__()
        self.classroom_service = classroom_service
        self.calendar_service = calendar_service
        self.drive_service = drive_service
        self._setup_student_tools()
    
    def _setup_student_tools(self):
        """Setup tools specific to student needs"""
        
        # Tool for getting assignments
        def get_assignments():
            if self.classroom_service:
                assignments = self.classroom_service.get_upcoming_assignments()
                return self._format_assignments(assignments)
            return "No classroom service available"
        
        # Tool for creating calendar reminders
        def create_reminder(task_name: str = "assignment", due_date: str = "tomorrow"):
            return f"Reminder created for {task_name} on {due_date}"
        
        # Tool for searching course materials
        def search_materials(query: str = "lecture notes"):
            if self.drive_service:
                files = self.drive_service.search_files(f"name contains '{query}'")
                return json.dumps(files[:5])  # Return top 5 results
            return "No drive service available"
        
        self.add_tool(get_assignments, "Get all upcoming assignments and due dates")
        self.add_tool(create_reminder, "Create calendar reminders for assignments")
        self.add_tool(search_materials, "Search for course materials in Google Drive")
    
    def _format_assignments(self, assignments: List[Dict]) -> str:
        """Format assignments for display"""
        if not assignments:
            return "No upcoming assignments"
        
        formatted = "Your assignments:\n"
        for assignment in assignments[:5]:  # Show top 5
            formatted += f"- {assignment.get('title', 'Untitled')} (Due: {assignment.get('dueDate', 'TBD')})\n"
        return formatted


class FacultyAgent(EduVoiceAgent):
    """Agent specialized for faculty interactions"""
    
    def __init__(self, classroom_service=None, calendar_service=None, gmail_service=None):
        super().__init__()
        self.classroom_service = classroom_service
        self.calendar_service = calendar_service
        self.gmail_service = gmail_service
        self._setup_faculty_tools()
    
    def _setup_faculty_tools(self):
        """Setup tools specific to faculty needs"""
        
        # Tool for scheduling classes
        def schedule_class(course_name: str = "Course", time: str = "tomorrow 10 AM"):
            return f"Class '{course_name}' scheduled for {time}"
        
        # Tool for sending announcements
        def send_announcement(announcement: str = "Demo announcement", recipients: str = "all students"):
            return f"Announcement sent to {recipients}"
        
        # Tool for creating assignments
        def create_assignment(title: str = "Assignment 1", due_date: str = "next week"):
            return f"Assignment '{title}' created with due date {due_date}"
        
        self.add_tool(schedule_class, "Schedule a class or revision session")
        self.add_tool(send_announcement, "Send announcements to students")
        self.add_tool(create_assignment, "Create and assign new assignments")


class AdminAgent(EduVoiceAgent):
    """Agent specialized for administrator interactions"""
    
    def __init__(self, sheets_service=None, gmail_service=None):
        super().__init__()
        self.sheets_service = sheets_service
        self.gmail_service = gmail_service
        self._setup_admin_tools()
    
    def _setup_admin_tools(self):
        """Setup tools specific to admin needs"""
        
        # Tool for generating reports
        def generate_report(report_type: str = "attendance"):
            return f"Generating {report_type} report..."
        
        # Tool for analyzing data
        def analyze_data(spreadsheet_id: str = "sheet123"):
            return f"Analyzing data from spreadsheet {spreadsheet_id}"
        
        # Tool for sending bulk emails
        def send_bulk_email(recipients: str = "all@college.edu", subject: str = "Important Notice"):
            return f"Bulk email sent to {recipients} with subject: {subject}"
        
        self.add_tool(generate_report, "Generate reports on attendance, performance, etc.")
        self.add_tool(analyze_data, "Analyze data from Google Sheets")
        self.add_tool(send_bulk_email, "Send bulk emails to staff/students")
