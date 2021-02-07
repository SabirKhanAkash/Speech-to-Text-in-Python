#Go to Terminal /cmd and type: python SpeechToText.py
# then start talking when screen says Recording ...

import speech_recognition as sr
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting Noises...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("How long you want to record (in seconds): ")
    time = int(input())
    print("Recording for ",time," seconds...")
    recorded_audio = recognizer.listen(source, timeout=time)
    print("Recording is done !")

    try:
        print("Recognizing the text from the recorded audio")
        text = recognizer.recognize_google(
            recorded_audio,
            language = "en-US"
        )
        print("Decoded text is: {}".format(text))

    except Exception as ex:
        print("Ooops! Something went wrong...")
        print(ex)
