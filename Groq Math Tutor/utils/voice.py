import speech_recognition as sr

def voice_to_text():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)
        text = recognizer.recognize_google(audio)
        return text
    except Exception as e:
        raise Exception(f"Voice Recognition Error: {str(e)}")
