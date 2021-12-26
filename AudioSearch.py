import speech_recognition as sr
parameter = str(input("PARAMETER"))
input = str(input("Filename:"))
r = sr.Recognizer()
with sr.AudioFile(input) as source:
    audio_text = r.listen(source)
    try:
        text = r.recognize_google(audio_text)
        if parameter in text:
            print("Confirmation:Parameter present in audioclip.")
    except:
        print('Error')