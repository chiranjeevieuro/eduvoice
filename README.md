# 🎤 EduVoice AI Assistant

> A voice-first, agentic AI solution for improving customer experience in digital education through Google Workspace integration.

**Built for:** Google Developers Group Hackathon (Hyderabad)

---

## Table of Contents

- [Overview](#overview)
- [Scenarios](#scenarios)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Technology Stack](#technology-stack)
- [Why This Solution Wins](#why-this-solution-wins)
- [Hackathon Highlights](#hackathon-highlights)

---

## Overview

Welcome! This demo showcases the **EduVoice AI Assistant** architecture built for the Google Developers Group Hackathon (Hyderabad).

EduVoice AI Assistant is a voice-first, agentic AI platform that:
- Understands natural language commands (voice & text)
- Takes intelligent actions through Google Workspace APIs
- Supports multiple user types (Students, Faculty, Administrators)
- Works in multiple languages (English, Telugu, Hindi)
- Improves customer experience in digital education

---

## Scenarios

### Scenario 1: Student Using EduVoice AI Assistant

**🎓 Student Request:**
```
"What assignments are due this week?"
```

**🤖 EduVoice Assistant Response:**

```
I'm checking your Google Classroom for upcoming assignments...

Your Assignments This Week:
✓ Machine Learning Homework - Due: Wednesday, 11:59 PM
✓ Linear Algebra Quiz - Due: Friday, 2:00 PM  
✓ Python Project - Due: Next Monday, 5:00 PM

I've added reminders to your Google Calendar for each one!
```

---

### Scenario 2: Faculty Using EduVoice AI Assistant

**👨‍🏫 Faculty Request:**
```
"Schedule a revision class for AI course tomorrow at 3 PM"
```

**🤖 EduVoice Assistant Response:**

```
Creating event in your calendar...

✓ Event Created: "AI Course Revision Class"
✓ Time: Tomorrow at 3:00 PM - 4:00 PM
✓ Google Meet Link: https://meet.google.com/abc-defg-hij
✓ Invitations sent to all 42 enrolled students

The event has been added to your calendar and student emails have been sent!
```

---

### Scenario 3: Administrator Using EduVoice AI Assistant

**👔 Admin Request:**
```
"Generate attendance report for Computer Science"
```

**🤖 EduVoice Assistant Response:**

```
Analyzing data from Google Sheets...

📊 CS Department Attendance Report
─────────────────────────────────
Total Students: 156
Average Attendance: 87.5%

Top Performers (95%+):
• Rahul Kumar - 98%
• Priya Singh - 97%
• Amit Patel - 96%

Needs Attention (<75%):
• Student ID 42 - 68%
• Student ID 87 - 71%
• Student ID 124 - 74%

Report saved to: CS_Attendance_Report_May2026.pdf
Email sent to department heads.
```

---

### Scenario 4: Multilingual Support - Telugu

**🌍 Student Request (in Telugu):**
```
"నాకు రేపు ఏ క్లాసులు ఉన్నాయి?"
(Translation: "What classes do I have tomorrow?")
```

**🤖 EduVoice Assistant Response (in Telugu):**

```
రేపు నీకు ఈ క్లాసులు ఉన్నాయి:

• ఉదయం 10:00 - AI ఉపన్యాసం
• సాయంత్రం 2:00 - గణిత కక్ష
• సాయంత్రం 4:00 - కంప్యూటర్ ల్యాబ్

మీ గూగిల్ క్యాలెండర్‌కు రిమైండర్‌లను జోడించాను!
```

---

## Key Features

| Feature | Description |
|---------|-------------|
| 🎤 **Voice-First Interface** | Natural language commands in voice or text |
| 🔗 **Google Workspace Integration** | Classroom, Calendar, Drive, Sheets, Gmail |
| 🤖 **Agentic AI** | Intelligent agents for Student, Faculty, Admin roles |
| 🌍 **Multilingual Support** | English, Telugu, Hindi with voice synthesis |
| 📱 **User-Specific Workflows** | Tailored experiences for different user types |
| ⚡ **Real-Time Actions** | Automatic calendar events, emails, reminders |

---

## Architecture

```
EduVoice AI Assistant
├── Voice Interface (Speech Recognition & TTS)
│   └── Text & Voice Input/Output
├── User Agents (Agentic AI with LangChain)
│   ├── StudentAgent (Assignments, Reminders, Materials)
│   ├── FacultyAgent (Classes, Announcements, Grading)
│   └── AdminAgent (Reports, Analytics, Communications)
├── Google Workspace APIs
│   ├── Classroom API (Assignments & Courses)
│   ├── Calendar API (Scheduling & Events)
│   ├── Sheets API (Data Analysis & Reports)
│   ├── Drive API (Document Management)
│   └── Gmail API (Communications)
└── LLM Backend (Google Generative AI - Gemini)
    └── Natural Language Understanding & Generation
```

---

## Quick Start

### Text Mode - Student
```bash
python main.py --user-type student --mode text
```

### Text Mode - Faculty
```bash
python main.py --user-type faculty --mode text
```

### Text Mode - Admin
```bash
python main.py --user-type admin --mode text
```

### Voice Mode
```bash
python main.py --user-type student --mode voice
```

### Demo Mode
```bash
python main.py --user-type student --demo
```

---

## Technology Stack

| Component | Technology |
|-----------|-----------|
| **LLM & NLP** | Google Generative AI (Gemini Pro), LangChain Agents |
| **Voice** | Google Cloud Speech-to-Text, Text-to-Speech |
| **APIs** | Google Workspace (Classroom, Calendar, Sheets, Drive, Gmail) |
| **Backend** | Python 3.11+, Flask, Firebase (optional) |
| **Frontend** | CLI (Text & Voice modes) |

---

## Why This Solution Wins

1. ✅ **Deeply integrated** with Google Workspace ecosystem
2. ✅ **Demonstrates agentic AI patterns** (not just chatbot)
3. ✅ **Voice-first design** improves accessibility & UX
4. ✅ **Solves real-world problem:** digital education transformation
5. ✅ **Multilingual support** for Indian context
6. ✅ **Ready for immediate deployment** and customization
7. ✅ **Complete architecture** with proper software engineering practices

---

## Hackathon Highlights

### This Solution:

- ✅ **Aligns with Google's ecosystem** (Workspace, Cloud, Generative AI)
- ✅ **Demonstrates advanced AI/agentic patterns**
- ✅ **Provides practical value** for educational institutions
- ✅ **Shows innovation** in voice-first UX design
- ✅ **Addresses the hackathon theme:** "Improving Customer Experience"

---

## 📎 Resources

- **Presentation:** [View Here](https://1drv.ms/p/c/59b9480cd8c619ee/IQD1DPzufccMT4q7nKMJ_RG-AWobW0-Ebiid3JWsi0U5TLs?e=k4qcGG)

---

<div align="center">

### ✨ Thank you for exploring EduVoice AI Assistant! ✨

**Built with ❤️ for the Google Developers Group Hackathon**

</div>