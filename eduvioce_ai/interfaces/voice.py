"""
Voice Interface Module
Handles speech recognition and text-to-speech
"""
import sys
from eduvioce_ai.utils import get_logger
from config.settings import VOICE_LANGUAGE, VOICE_SPEED
from typing import Optional

logger = get_logger(__name__)

# Optional imports for voice support
try:
    import speech_recognition as sr
    HAS_SPEECH_RECOGNITION = True
except ImportError:
    HAS_SPEECH_RECOGNITION = False
    logger.warning("speech_recognition not installed - voice input disabled")

try:
    import pyttsx3
    HAS_PYTTSX3 = True
except ImportError:
    HAS_PYTTSX3 = False
    logger.warning("pyttsx3 not installed - voice output disabled")

class VoiceInterface:
    """Handles voice input and output"""
    
    def __init__(self, language: str = VOICE_LANGUAGE):
        if not HAS_SPEECH_RECOGNITION or not HAS_PYTTSX3:
            logger.warning("Voice interface partially available - some features disabled")
            if not HAS_SPEECH_RECOGNITION:
                logger.warning("Install SpeechRecognition for voice input: pip install SpeechRecognition")
            if not HAS_PYTTSX3:
                logger.warning("Install pyttsx3 for voice output: pip install pyttsx3")
        
        self.language = language
        
        if HAS_SPEECH_RECOGNITION:
            self.recognizer = sr.Recognizer()
        else:
            self.recognizer = None
        
        if HAS_PYTTSX3:
            self.tts_engine = pyttsx3.init()
            self.tts_engine.setProperty('rate', VOICE_SPEED * 150)
        else:
            self.tts_engine = None
        
        logger.info(f"VoiceInterface initialized with language: {language}")
    
    def listen(self, timeout: int = 10) -> Optional[str]:
        """Capture voice input and convert to text"""
        if not HAS_SPEECH_RECOGNITION or not self.recognizer:
            logger.warning("Voice input not available - install SpeechRecognition")
            return None
        
        try:
            with sr.Microphone() as source:
                logger.info("Listening for voice input...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=timeout)
            
            # Try multiple recognition services
            try:
                text = self.recognizer.recognize_google(audio, language=self.language)
                logger.info(f"Recognized text: {text}")
                return text
            except sr.UnknownValueError:
                logger.warning("Could not understand audio")
                return None
            except sr.RequestError as e:
                logger.error(f"Error with recognition service: {e}")
                return None
                
        except sr.RequestError as e:
            logger.error(f"Microphone error: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error during listening: {e}")
            return None
    
    def speak(self, text: str):
        """Convert text to speech and play"""
        if not HAS_PYTTSX3 or not self.tts_engine:
            logger.warning("Voice output not available - install pyttsx3")
            return
        
        try:
            logger.info(f"Speaking: {text}")
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            logger.error(f"Error during text-to-speech: {e}")
    
    def set_language(self, language_code: str):
        """Set language for voice recognition"""
        self.language = language_code
        logger.info(f"Language set to: {language_code}")
    
    def voice_input_with_confirmation(self) -> Optional[str]:
        """Capture voice input with confirmation"""
        text = self.listen()
        if text:
            self.speak(f"I heard: {text}. Is this correct?")
            confirmation = self.listen(timeout=5)
            if confirmation and confirmation.lower() in ["yes", "yeah", "correct", "right"]:
                return text
            else:
                self.speak("Let's try again.")
                return self.voice_input_with_confirmation()
        return None


class TextInterface:
    """Fallback text-based interface"""
    
    def __init__(self):
        logger.info("TextInterface initialized")
    
    def input_text(self, prompt: str = "Enter your request: ") -> str:
        """Get text input from user"""
        return input(prompt)
    
    def output_text(self, text: str):
        """Display text output"""
        print(f"Assistant: {text}")
