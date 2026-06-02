# EduVoice AI Assistant 🎤

A **voice-first, agentic AI application** built for the **Google Developers Group Hackathon** (Hyderabad) - Designed to improve customer experience in digital education using **Google Workspace** integration and advanced AI.

## 🎯 Project Overview

**EduVoice AI Assistant** is a multilingual, voice-first application that transforms how colleges deliver digital education. It leverages:

- **Google Workspace APIs** (Classroom, Calendar, Sheets, Drive, Gmail)
- **Agentic AI** using LangChain and Google Generative AI
- **Voice Recognition & Synthesis** for accessibility
- **User-Specific Agents** for Students, Faculty, and Administrators

### Key Features

✨ **Voice-First Interface** - Natural language voice commands  
🎓 **Student Assistant** - Assignments, schedules, course materials  
👨‍🏫 **Faculty Tools** - Class scheduling, announcements, grading  
📊 **Admin Dashboard** - Reports, analytics, bulk communications  
🌍 **Multilingual Support** - English, Telugu, Hindi  
🤖 **Agentic AI** - Automated workflows and decision-making  

---

## 📋 Prerequisites

- **Python 3.9+** (tested with Python 3.11.4)
- **Google Cloud Account** with Workspace APIs enabled
- **Microphone** (for voice input)
- **Google OAuth Credentials** (for Workspace integration)

---

## 🚀 Quick Start

### 1. Clone/Setup Project

```bash
cd "THE PARK APL-VOICE FIRST APP"
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy `.env.example` to `.env` and update with your settings:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:
- `GOOGLE_APPLICATION_CREDENTIALS` - Path to your Google service account JSON
- `GOOGLE_CLOUD_PROJECT` - Your Google Cloud project ID
- `GENAI_API_KEY` - Your Google Generative AI API key

### 5. Setup Google Workspace Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project and enable:
   - Google Classroom API
   - Google Calendar API
   - Google Sheets API
   - Google Drive API
   - Gmail API
3. Create OAuth 2.0 credentials (Desktop application)
4. Download and save as `credentials.json` in project root

### 6. Run Demo (Text Mode - No Voice Required)

```bash
python demo.py
```

This will show example interactions for all three user types without requiring voice or Google services.

---

## 📖 Usage Examples

### For Students

**Text Mode:**
```bash
python main.py --user-type student --mode text
```

Then interact naturally:
```
You: What assignments are due this week?
Assistant: You have Machine Learning homework due Wednesday and a Math quiz on Friday...

You: Create a reminder for my math homework
Assistant: Reminder created successfully...

You: Find my AI lecture notes
Assistant: I found 5 documents related to AI lectures in your Drive...
```

**Voice Mode:**
```bash
python main.py --user-type student --mode voice
```

Simply speak your requests!

### For Faculty

```bash
python main.py --user-type faculty --mode text
```

Example requests:
- "Schedule a revision class for tomorrow at 3 PM"
- "Send an announcement to my students about the exam"
- "Create an assignment on quantum computing"

### For Administrators

```bash
python main.py --user-type admin --mode text
```

Example requests:
- "Generate attendance report for Computer Science this semester"
- "Analyze enrollment trends"
- "Send bulk email to all staff with semester updates"

### Demo Mode (No Google Services Required)

```bash
python main.py --user-type student --demo
python demo.py  # Interactive demo
```

---

## 📁 Project Structure

```
THE PARK APL-VOICE FIRST APP/
├── main.py                          # Application entry point
├── demo.py                          # Interactive demo script
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variables template
├── credentials.json                 # Google OAuth credentials (add your own)
├── README.md                        # This file
│
├── config/
│   ├── __init__.py
│   └── settings.py                  # Configuration and settings
│
├── eduvioce_ai/
│   ├── __init__.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   └── application.py           # Core application logic
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   └── agents.py                # Agentic AI implementations
│   │                                  (StudentAgent, FacultyAgent, AdminAgent)
│   │
│   ├── interfaces/
│   │   ├── __init__.py
│   │   └── voice.py                 # Voice interface & text fallback
│   │
│   ├── google_workspace/
│   │   ├── __init__.py
│   │   ├── auth.py                  # Google OAuth authentication
│   │   └── services.py              # Workspace API integrations
│   │                                  (Classroom, Calendar, Sheets, Drive, Gmail)
│   │
│   └── utils/
│       ├── __init__.py
│       └── logger.py                # Logging utilities
│
└── tests/
    └── (test files - to be added)
```

---

## 🔧 Architecture

### Components

1. **EduVoiceCore** - Main orchestrator
   - Manages user setup
   - Coordinates between interfaces and agents
   - Handles Google service initialization

2. **User Agents** (Agentic AI)
   - `StudentAgent` - Assignment tracking, reminders, material search
   - `FacultyAgent` - Class scheduling, announcements, assignments
   - `AdminAgent` - Reports, analytics, communications

3. **Interfaces**
   - `VoiceInterface` - Speech recognition & text-to-speech
   - `TextInterface` - Console-based text input/output

4. **Google Workspace Services**
   - Classroom API - Assignment and course management
   - Calendar API - Event scheduling
   - Sheets API - Data storage and analysis
   - Drive API - Document management
   - Gmail API - Email communications

### Agent Flow

```
User Input (Voice/Text)
    ↓
VoiceInterface/TextInterface
    ↓
EduVoiceCore
    ↓
User-Specific Agent (StudentAgent/FacultyAgent/AdminAgent)
    ↓
LangChain Agent with Tools
    ↓
Google Generative AI (Gemini)
    ↓
Tool Execution (Google Workspace APIs)
    ↓
Response Generation
    ↓
VoiceInterface/TextInterface
    ↓
User Output (Voice/Text)
```

---

## 🎯 Supported User Types & Commands

### Student
- ✅ View upcoming assignments
- ✅ Set assignment reminders
- ✅ Search course materials
- ✅ Check class schedules
- ✅ Get assignment deadlines

### Faculty
- ✅ Schedule revision classes
- ✅ Send class announcements
- ✅ Create assignments
- ✅ Manage attendance
- ✅ Communicate with students

### Administrator
- ✅ Generate attendance reports
- ✅ Analyze enrollment data
- ✅ Send bulk communications
- ✅ View institutional analytics
- ✅ Manage user accounts

---

## 🌍 Multilingual Support

Supported languages:
- 🇬🇧 English (en-US)
- 🇮🇳 Telugu (te-IN)
- 🇮🇳 Hindi (hi-IN)

Change language by updating `VOICE_LANGUAGE` in `.env`:
```
VOICE_LANGUAGE=te-IN  # For Telugu
```

---

## 🔐 Security Considerations

- Store `credentials.json` safely (never commit to git)
- Use environment variables for sensitive data
- OAuth tokens are automatically refreshed
- Add `credentials.json` and `.env` to `.gitignore`

---

## 📚 Technologies Used

### AI & NLP
- **Google Generative AI (Gemini)** - LLM backend
- **LangChain** - Agentic AI framework
- **Google Cloud Dialogflow** - (Optional) Advanced NLU

### Voice
- **SpeechRecognition** - Voice-to-text
- **pyttsx3** - Text-to-speech
- **PyAudio** - Audio input

### APIs
- **Google Workspace APIs** - Classroom, Calendar, Sheets, Drive, Gmail
- **Google Cloud** - Cloud services

### Backend
- **Flask** - (Optional) Web server
- **Firebase Admin** - (Optional) Real-time database

---

## 🐛 Troubleshooting

### Microphone Not Working
```bash
# Install PyAudio for your system
pip install --upgrade pyaudio
```

### Google API Errors
- Ensure `GOOGLE_APPLICATION_CREDENTIALS` points to valid credentials
- Check that all required APIs are enabled in Google Cloud Console
- Verify OAuth token has not expired

### Dependencies Installation Issues
```bash
# Clear pip cache and reinstall
pip cache purge
pip install -r requirements.txt --force-reinstall
```

### Module Import Errors
```bash
# Ensure project root is in Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

---

## 🚀 Future Enhancements

- 📱 Mobile app (React Native)
- 🌐 Web dashboard (React.js)
- 🔔 Push notifications
- 📊 Advanced analytics dashboard
- 🎮 Gamification for student engagement
- 📋 PDF lecture notes auto-summarization
- 🎥 Video lecture transcription
- 💬 Group chat integration
- 📅 Calendar synchronization

---

## 👥 Contributing

Contributions welcome! Please follow:
1. PEP 8 style guide
2. Add docstrings to all functions
3. Include unit tests for new features
4. Update README for significant changes

---

## 📄 License

This project is developed for the Google Developers Group Hackathon (Hyderabad).

---

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review Google Workspace API documentation
3. Check LangChain documentation
4. Open an issue with detailed error messages

---

## 🎓 Educational Impact

**EduVoice AI Assistant** demonstrates:
- Integration of multiple Google APIs
- Agentic AI patterns with LangChain
- Voice-first UX design
- Multilingual AI applications
- Real-world hackathon implementation

Perfect for showcasing at the **Google Developers Group Hackathon** with judges looking for innovative, Google-ecosystem-aligned solutions! 🏆

---

**Made with ❤️ for Digital Education Transformation**
