from datetime import datetime
import pyttsx3
import edge_tts

VOICE = "en-US-EmmaNeural"

OUTPUT_FILE = f"{datetime.now().strftime('%m%d%Y%H%M%S')}.mp3"


def read_w_edge_tts(content_to_read: str) -> None:
    communicate = edge_tts.Communicate(content_to_read, VOICE, rate="+15%")
    communicate.save_sync(OUTPUT_FILE)
    print(f"saved {OUTPUT_FILE}\n")


class Narrator():
    def __init__(self, gender_voice = None):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty("voices")
        if gender_voice:
            self.voice = self.engine.setProperty("voice", gender_voice)
        else:
            self.voice = self.engine.setProperty("voice", self.voices[0].id)

    def read(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def change_voice(self, i):
        self.engine.setProperty("voice", self.voices[i].id)
