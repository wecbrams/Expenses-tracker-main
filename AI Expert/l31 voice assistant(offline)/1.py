import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import pyttsx3
import json
import datetime
import sys

# Initialize the Vosk model and TTS engine
model = Model("model")  # path to your Vosk model folder
recognizer = KaldiRecognizer(model, 16000)
audio_queue = queue.Queue()
tts_engine = pyttsx3.init()

# Callback function to capture audio data
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(bytes(indata))

# Function to process user input and respond
def process_query(query):
    query = query.lower()

    if "time" in query:
        now = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {now}."

    elif "date" in query:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today's date is {today}."

    elif "exit" in query or "quit" in query:
        return "Goodbye."

    else:
        return "I'm sorry, I didn't understand that."

print("Listening... Say 'time', 'date', or 'exit'.")

# Open the audio stream
with sd.RawInputStream(
    samplerate=16000,
    blocksize=8000,
    dtype="int16",
    channels=1,
    callback=callback,
):

    while True:
        data = audio_queue.get()

        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")

            if text:
                print(f"You said: {text}")

                response = process_query(text)
                print(f"Assistant: {response}")

                tts_engine.say(response)
                tts_engine.runAndWait()

                if "goodbye" in response.lower():
                    break


"""
pip install sounddevice
pip install SpeechRecognition

pip install pyttsx3

pip install googletrans==4.0.0-rc1

pip install pyaudio
pip install vosk

"""