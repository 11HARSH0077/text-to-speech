from gtts import gTTS
text=" Hello, i am harsh garg "
language="en"
obj=gTTS(text=text,lang=language,slow=False)
obj.save("sample.mp3")
