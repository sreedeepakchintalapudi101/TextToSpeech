from gtts import gTTS
from playsound import playsound
audio = "speech.mp3"
language = "en"
sp = gTTS(text = "Hi, My name is Sree Deepak Chintalapudi",lang = language, slow = False)
sp.save(audio)
playsound(audio)
print("=====AUDIO IS PLAYING=====")
