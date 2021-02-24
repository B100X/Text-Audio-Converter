from gtts import gTTS
# pip instal gtts

from playsound import playsound
# pip install playsound

audio = 'audio-name.mp3'
language = 'en'
sp = gTTS(text = "Enter your text which you want to convert into audio file",
          lang = language,slow=False)

sp.save(audio)
playsound(audio)
