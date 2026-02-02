# ===============================
# Voice Analysis Lab
# Record → Analyze → Compare
# ===============================

import threading
import sys
import numpy as np
import pyaudio
import matplotlib.pyplot as plt
import speech_recognition as sr
from speech_recognition import AudioData

# Global stop flag for recording
stop_event = threading.Event()

def wait_for_enter():
    input()
    stop_event.set()

# -------------------------------
# Record audio until Enter pressed
# -------------------------------
def record_audio(label):
    stop_event.clear()
    p = pyaudio.PyAudio()

    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=1024
    )

    frames = []

    print(f"\n🎙️ {label}")
    print("Press Enter to stop recording...")
    threading.Thread(target=wait_for_enter, daemon=True).start()

    while not stop_event.is_set():
        frames.append(stream.read(1024, exception_on_overflow=False))

    stream.stop_stream()
    stream.close()
    p.terminate()

    width = p.get_sample_size(pyaudio.paInt16)
    return b"".join(frames), 16000, width

# -------------------------------
# Analyze audio properties
# -------------------------------
def analyze_audio(data, rate):
    samples = np.frombuffer(data, dtype=np.int16)

    return {
        "duration": len(samples) / rate,
        "avg_volume": np.mean(np.abs(samples)),
        "max_volume": np.max(np.abs(samples)),
        "samples": samples
    }

# -------------------------------
# Transcribe speech
# -------------------------------
def transcribe(data, rate, width):
    recognizer = sr.Recognizer()
    try:
        return recognizer.recognize_google(AudioData(data, rate, width))
    except:
        return "[Transcription failed]"

# -------------------------------
# Display stats
# -------------------------------
def display_stats(stats, text, label):
    print("\n" + "-" * 40)
    print(f"📊 {label}")
    print("-" * 40)
    print(f"Duration: {stats['duration']:.2f} seconds")
    print(f"Average Amplitude: {stats['avg_volume']:.0f}")
    print(f"Maximum Amplitude: {stats['max_volume']:.0f}")
    print(f"Transcription: {text}")

# -------------------------------
# Compare two recordings
# -------------------------------
def compare(stats1, stats2):
    print("\n" + "=" * 40)
    print("🔍 COMPARISON RESULTS")
    print("=" * 40)

    dur_diff = ((stats2["duration"] - stats1["duration"]) / stats1["duration"]) * 100
    vol_diff = ((stats2["avg_volume"] - stats1["avg_volume"]) / stats1["avg_volume"]) * 100

    print(f"Duration change: {dur_diff:+.1f}%")
    print(f"Average volume change: {vol_diff:+.1f}%")

# -------------------------------
# Plot waveforms
# -------------------------------
def plot_waveforms(stats1, stats2, rate):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))

    t1 = np.linspace(0, stats1["duration"], len(stats1["samples"]))
    ax1.plot(t1, stats1["samples"])
    ax1.set_title("Recording 1 - Normal Voice")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True)

    t2 = np.linspace(0, stats2["duration"], len(stats2["samples"]))
    ax2.plot(t2, stats2["samples"])
    ax2.set_title("Recording 2 - Modified Voice")
    ax2.set_xlabel("Time (seconds)")
    ax2.set_ylabel("Amplitude")
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

# -------------------------------
# Main program
# -------------------------------
def main():
    print("🎧 VOICE ANALYSIS LAB")
    print("Record twice and compare your voice!")

    audio1, rate, width = record_audio("Recording 1: Speak normally")
    stats1 = analyze_audio(audio1, rate)
    text1 = transcribe(audio1, rate, width)
    display_stats(stats1, text1, "Recording 1 Results")

    input("\nPress Enter to record again (speak louder or faster)...")

    audio2, rate, width = record_audio("Recording 2: Change your voice")
    stats2 = analyze_audio(audio2, rate)
    text2 = transcribe(audio2, rate, width)
    display_stats(stats2, text2, "Recording 2 Results")

    compare(stats1, stats2)
    plot_waveforms(stats1, stats2, rate)

# -------------------------------
if __name__ == "__main__":
    main()
