"""
Demo script showing EduVoice AI Assistant capabilities
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from eduvioce_ai.core import EduVoiceCore
from eduvioce_ai.utils import get_logger

logger = get_logger(__name__)

def demo_student():
    """Demo for student user"""
    print("\n" + "="*60)
    print("DEMO: Student Using EduVoice AI Assistant")
    print("="*60)
    
    app = EduVoiceCore(use_voice=False)  # Text mode for demo
    app.setup_user('student', use_voice=False)
    
    demo_requests = [
        "What assignments are due this week?",
        "Create a reminder for my math homework",
        "Find my AI lecture notes",
    ]
    
    for request in demo_requests:
        print(f"\n📝 Student: {request}")
        response = app.process_user_request(request)
        print(f"🤖 Assistant: {response}")


def demo_faculty():
    """Demo for faculty user"""
    print("\n" + "="*60)
    print("DEMO: Faculty Using EduVoice AI Assistant")
    print("="*60)
    
    app = EduVoiceCore(use_voice=False)  # Text mode for demo
    app.setup_user('faculty', use_voice=False)
    
    demo_requests = [
        "Schedule a revision class for tomorrow at 3 PM",
        "Send an announcement to my students",
        "Create an assignment for the AI course",
    ]
    
    for request in demo_requests:
        print(f"\n📝 Faculty: {request}")
        response = app.process_user_request(request)
        print(f"🤖 Assistant: {response}")


def demo_admin():
    """Demo for admin user"""
    print("\n" + "="*60)
    print("DEMO: Administrator Using EduVoice AI Assistant")
    print("="*60)
    
    app = EduVoiceCore(use_voice=False)  # Text mode for demo
    app.setup_user('admin', use_voice=False)
    
    demo_requests = [
        "Generate an attendance report for Computer Science this semester",
        "Analyze enrollment data",
        "Send a bulk email to all staff",
    ]
    
    for request in demo_requests:
        print(f"\n📝 Admin: {request}")
        response = app.process_user_request(request)
        print(f"🤖 Assistant: {response}")


def main():
    """Run all demos"""
    print("\n" + "🎤 " + "="*56 + " 🎤")
    print("   Welcome to EduVoice AI Assistant - Demo")
    print("🎤 " + "="*56 + " 🎤\n")
    
    try:
        demo_student()
        demo_faculty()
        demo_admin()
        
        print("\n" + "="*60)
        print("✅ Demo completed successfully!")
        print("="*60)
        print("\nTo run the full application:")
        print("  - For text mode: python main.py --user-type student --mode text")
        print("  - For voice mode: python main.py --user-type student --mode voice")
        print("  - For demo mode: python main.py --user-type student --demo")
        print("\n")
        
    except Exception as e:
        logger.error(f"Error in demo: {e}")
        print(f"\n❌ Demo error: {e}")


if __name__ == '__main__':
    main()
