# VOICE ANALYSIS LAB
# Record → Analyze → Compare Voice
# pip install pyaudio SpeechRecognition

import sys
import threading

# DEPENDENCY CHECK
try:
    import pyaudio
    import numpy as np
    import matplotlib.pyplot as plt
    import speech_recognition as sr
    from speech_recognition import AudioData
except ImportError as e:
    print(f"❌ Missing library: {e.name}")
    print("\n📦 Install using:")
    print("Windows: pip install SpeechRecognition pyaudio numpy matplotlib")
    print("macOS: brew install portaudio && pip install SpeechRecognition pyaudio numpy matplotlib")
    sys.exit(1)


# GLOBAL STOP EVENT

stop_event = threading.Event()

def wait_for_enter():
    input()
    stop_event.set()


# RECORD AUDIO FUNCTION

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
    print(f"\n🎤 {label}")
    print("Press ENTER to stop recording...")

    threading.Thread(target=wait_for_enter, daemon=True).start()

    print("Recording", end="", flush=True)
    while not stop_event.is_set():
        frames.append(stream.read(1024, exception_on_overflow=False))
        print(".", end="", flush=True)

    print("\nRecording stopped.")

    stream.stop_stream()
    stream.close()
    sample_width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()

    audio_data = b"".join(frames)
    return audio_data, 16000, sample_width


# ANALYZE AUDIO FUNCTION

def analyze_audio(data, rate):
    samples = np.frombuffer(data, dtype=np.int16)

    return {
        "duration": len(samples) / rate,
        "avg_volume": np.mean(np.abs(samples)),
        "max_volume": np.max(np.abs(samples)),
        "samples": samples
    }


# TRANSCRIBE AUDIO FUNCTION

def transcribe_audio(data, rate, width):
    recognizer = sr.Recognizer()
    audio = AudioData(data, rate, width)

    try:
        return recognizer.recognize_google(audio)
    except:
        return "[Could not transcribe speech]"


# DISPLAY STATS FUNCTION

def display_stats(stats, text, label):
    print("\n" + "-" * 40)
    print(f"📊 {label}")
    print("-" * 40)
    print(f"⏱ Duration: {stats['duration']:.2f} seconds")
    print(f"📈 Average Amplitude: {stats['avg_volume']:.0f}")
    print(f"🚀 Maximum Amplitude: {stats['max_volume']:.0f}")
    print(f"📝 Transcription: {text}")
# COMPARE RECORDINGS
def compare_recordings(stats1, stats2):
    print("\n" + "=" * 40)
    print("🔍 COMPARISON RESULTS")
    print("=" * 40)

    if stats1["duration"] > stats2["duration"]:
        diff = ((stats1["duration"] - stats2["duration"]) / stats2["duration"]) * 100
        print(f"⏱ Recording 1 is longer by {diff:.1f}%")
    else:
        diff = ((stats2["duration"] - stats1["duration"]) / stats1["duration"]) * 100
        print(f"⏱ Recording 2 is longer by {diff:.1f}%")

    if stats1["avg_volume"] > stats2["avg_volume"]:
        diff = ((stats1["avg_volume"] - stats2["avg_volume"]) / stats2["avg_volume"]) * 100
        print(f"🔊 Recording 1 is louder by {diff:.1f}%")
    else:
        diff = ((stats2["avg_volume"] - stats1["avg_volume"]) / stats1["avg_volume"]) * 100
        print(f"🔊 Recording 2 is louder by {diff:.1f}%")
# PLOT BOTH WAVEFORMS
def plot_waveforms(stats1, stats2, rate):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))

    t1 = np.linspace(0, len(stats1["samples"]) / rate, len(stats1["samples"]))
    ax1.plot(t1, stats1["samples"], linewidth=0.5)
    ax1.set_title("Recording 1 - Normal Voice")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True)

    t2 = np.linspace(0, len(stats2["samples"]) / rate, len(stats2["samples"]))
    ax2.plot(t2, stats2["samples"], linewidth=0.5)
    ax2.set_title("Recording 2 - Changed Voice")
    ax2.set_xlabel("Time (seconds)")
    ax2.set_ylabel("Amplitude")
    ax2.grid(True)

    plt.tight_layout()
    plt.show()


# MAIN PROGRAM

def main():
    print("=" * 40)
    print("🎧 VOICE ANALYSIS LAB")
    print("=" * 40)
    print("Record two samples and compare your voice!\n")

    audio1, rate, width = record_audio("Recording 1: Speak normally")
    stats1 = analyze_audio(audio1, rate)
    text1 = transcribe_audio(audio1, rate, width)
    display_stats(stats1, text1, "Recording 1 Results")

    input("\n👉 Press ENTER, then speak louder or faster...")

    audio2, rate, width = record_audio("Recording 2: Change your voice!")
    stats2 = analyze_audio(audio2, rate)
    text2 = transcribe_audio(audio2, rate, width)
    display_stats(stats2, text2, "Recording 2 Results")

    compare_recordings(stats1, stats2)
    plot_waveforms(stats1, stats2, rate)


# RUN PROGRAM

if __name__ == "__main__":
    main()
