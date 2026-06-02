# 🚀 Quick Start Guide - EduVoice AI Assistant

## Step 1: Install Dependencies

Open PowerShell in the project directory and run:

```powershell
pip install -r requirements.txt
```

This will install all required packages including:
- Google APIs
- LangChain and Google Generative AI
- Speech Recognition & Text-to-Speech
- Flask and other utilities

**Installation takes approximately 3-5 minutes.**

## Step 2: Configure Environment Variables

1. Copy `.env.example` to `.env`:
```powershell
copy .env.example .env
```

2. Edit `.env` with your settings (optional for demo):
```
APP_DEBUG=True
APP_PORT=5000
VOICE_LANGUAGE=en-US
GENAI_API_KEY=your-api-key-here
```

## Step 3: Try the Demo (No Configuration Needed!)

### Option A: Quick Demo (Recommended for First Time)

```powershell
python demo.py
```

This runs example interactions for all user types without needing Google services or voice input.

### Option B: Interactive Text Mode

**For Students:**
```powershell
python main.py --user-type student --mode text --demo
```

**For Faculty:**
```powershell
python main.py --user-type faculty --mode text --demo
```

**For Administrators:**
```powershell
python main.py --user-type admin --mode text --demo
```

## Step 4: Setup Google Integration (Optional)

To use real Google Workspace APIs:

1. **Get Google API Credentials:**
   - Go to https://console.cloud.google.com/
   - Create a new project
   - Enable APIs: Classroom, Calendar, Sheets, Drive, Gmail
   - Create OAuth 2.0 Desktop credentials
   - Download JSON and save as `credentials.json`

2. **Set up your `.env` file:**
   ```
   GOOGLE_APPLICATION_CREDENTIALS=credentials.json
   GOOGLE_CLOUD_PROJECT=your-project-id
   GENAI_API_KEY=your-genai-api-key
   ```

3. **Run with Google Services:**
   ```powershell
   python main.py --user-type student --mode text
   ```

## Voice Mode (Optional)

If you have a microphone:

```powershell
python main.py --user-type student --mode voice
```

**Note:** Requires `pyaudio` which may need additional setup on Windows. For demo purposes, use text mode.

## Troubleshooting

### Import Errors
```powershell
set PYTHONPATH=%PYTHONPATH%;.
python demo.py
```

### Missing Dependencies
```powershell
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Google API Errors
- Ensure credentials.json exists and is valid
- Check all required APIs are enabled in Google Cloud Console
- Verify your API keys in .env

## Project Structure

```
THE PARK APL-VOICE FIRST APP/
├── main.py              # Main application
├── demo.py              # Demo script (START HERE!)
├── requirements.txt     # Dependencies
├── README.md           # Full documentation
├── QUICKSTART.md       # This file
│
├── eduvioce_ai/        # Main package
│   ├── core/           # Core application logic
│   ├── agents/         # AI agents (Student, Faculty, Admin)
│   ├── interfaces/     # Voice & text interfaces
│   ├── google_workspace/  # Google APIs
│   └── utils/          # Helper functions
│
└── config/             # Configuration files
```

## Example Interactions

### Student Mode
```
Student: What assignments are due this week?
Assistant: You have 3 assignments due this week...

Student: Create a reminder for my homework
Assistant: Reminder created successfully...
```

### Faculty Mode
```
Faculty: Schedule a class tomorrow at 3 PM
Assistant: Class scheduled successfully...

Faculty: Send announcement to students
Assistant: Announcement sent to all students...
```

### Admin Mode
```
Admin: Generate attendance report
Assistant: Generating report... [shows stats]

Admin: Analyze enrollment data
Assistant: Here are the enrollment trends...
```

## Next Steps

✅ Run `python demo.py` to see the app in action  
✅ Explore the code in `eduvioce_ai/` folder  
✅ Configure Google Workspace integration  
✅ Customize the application for your needs  

---

**Questions?** Check README.md for detailed documentation or explore the well-commented code!

**Ready to present at the hackathon?** The demo is fully functional and requires no setup! 🎤🎓
