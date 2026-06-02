"""
Unit tests for EduVoice AI Assistant
"""
import unittest
from unittest.mock import Mock, patch
from eduvioce_ai.core import EduVoiceCore, UserType
from eduvioce_ai.interfaces.voice import TextInterface
from eduvioce_ai.agents import StudentAgent, FacultyAgent, AdminAgent


class TestUserType(unittest.TestCase):
    """Test UserType enum"""
    
    def test_user_types_exist(self):
        self.assertEqual(UserType.STUDENT.value, "student")
        self.assertEqual(UserType.FACULTY.value, "faculty")
        self.assertEqual(UserType.ADMIN.value, "admin")


class TestEduVoiceCore(unittest.TestCase):
    """Test core application logic"""
    
    def setUp(self):
        self.app = EduVoiceCore(use_voice=False)
    
    def test_initialization(self):
        self.assertIsNotNone(self.app)
        self.assertFalse(self.app.use_voice)
        self.assertIsNone(self.app.user_type)
    
    def test_setup_student(self):
        result = self.app.setup_user('student', use_voice=False)
        self.assertTrue(result)
        self.assertEqual(self.app.user_type, UserType.STUDENT)
        self.assertIsNotNone(self.app.agent)
    
    def test_setup_faculty(self):
        result = self.app.setup_user('faculty', use_voice=False)
        self.assertTrue(result)
        self.assertEqual(self.app.user_type, UserType.FACULTY)
    
    def test_setup_admin(self):
        result = self.app.setup_user('admin', use_voice=False)
        self.assertTrue(result)
        self.assertEqual(self.app.user_type, UserType.ADMIN)
    
    def test_invalid_user_type(self):
        result = self.app.setup_user('invalid', use_voice=False)
        self.assertFalse(result)


class TestTextInterface(unittest.TestCase):
    """Test text interface"""
    
    def setUp(self):
        self.interface = TextInterface()
    
    def test_initialization(self):
        self.assertIsNotNone(self.interface)
    
    @patch('builtins.input', return_value='test input')
    def test_input_text(self, mock_input):
        result = self.interface.input_text()
        self.assertEqual(result, 'test input')
    
    @patch('builtins.print')
    def test_output_text(self, mock_print):
        self.interface.output_text("Test message")
        mock_print.assert_called_once()


class TestStudentAgent(unittest.TestCase):
    """Test student agent"""
    
    def test_student_agent_creation(self):
        agent = StudentAgent()
        self.assertIsNotNone(agent)
        self.assertTrue(len(agent.tools) > 0)


class TestFacultyAgent(unittest.TestCase):
    """Test faculty agent"""
    
    def test_faculty_agent_creation(self):
        agent = FacultyAgent()
        self.assertIsNotNone(agent)
        self.assertTrue(len(agent.tools) > 0)


class TestAdminAgent(unittest.TestCase):
    """Test admin agent"""
    
    def test_admin_agent_creation(self):
        agent = AdminAgent()
        self.assertIsNotNone(agent)
        self.assertTrue(len(agent.tools) > 0)


if __name__ == '__main__':
    unittest.main()
