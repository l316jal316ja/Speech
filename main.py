import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Iltimos, o'zbek tilida nimadir ayting...")
    audio_data = recognizer.listen(source)
    print("Taniyapman...")

    try:
        text = recognizer.recognize_google(audio_data, language="uz-UZ")
        print("Siz aytdingiz:", text)
    except sr.UnknownValueError:
        print("Kechirasiz, ovozni tushunib bo'lmadi.")
    except sr.RequestError:
        print("Google nutqni tanish xizmati bilan bog'lanib bo'lmadi.")
