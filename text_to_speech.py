import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init() 

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  

    engine.setProperty('rate', 150)   
    engine.setProperty('volume', 1.0)  

    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print("🧠 Text to Voice Converter")
    user_text = input("Enter the text you want to convert to speech:\n")
    text_to_speech(user_text)
