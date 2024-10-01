import pyttsx3


class Narrator():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty("voices")
        self.voice = self.engine.setProperty("voice", self.voices[0].id)

    def read(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def change_voice(self, i):
        self.engine.setProperty("voice", self.voices[i].id)
