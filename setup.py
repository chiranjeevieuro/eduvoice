"""
Setup script for EduVoice AI Assistant
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="eduvioce-ai",
    version="1.0.0",
    author="EduVoice Team",
    description="Voice-first agentic AI assistant for educational institutions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education",
    ],
    python_requires=">=3.9",
    install_requires=[
        "google-auth-oauthlib>=1.2.0",
        "google-auth-httplib2>=0.2.0",
        "google-api-python-client>=2.100.0",
        "google-cloud-speech>=2.21.1",
        "google-cloud-texttospeech>=2.14.1",
        "google-generativeai>=0.4.1",
        "langchain>=0.1.14",
        "langchain-google-genai>=0.0.12",
        "python-dotenv>=1.0.0",
        "SpeechRecognition>=3.10.0",
        "pyttsx3>=2.90",
        "requests>=2.31.0",
        "numpy>=1.24.3",
        "pandas>=2.0.3",
    ],
    entry_points={
        "console_scripts": [
            "eduvioce=main:main",
        ],
    },
)
