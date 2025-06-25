import sounddevice as sd
import numpy as np
import wave
from faster_whisper import WhisperModel
import datetime

SAMPLE_RATE = 16000
DURATION = 5
MODEL_SIZE = "base"
NOTES_FILE = "notes.txt"

def record_audio(duration=DURATION, sample_rate=SAMPLE_RATE):
    print(f"[🎙️] Recording for {duration} seconds...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    return recording

def save_wav(filename, data, sample_rate=SAMPLE_RATE):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(data.tobytes())
    print(f"[💾] Audio saved to {filename}")

def transcribe_audio(model, filename):
    segments, _ = model.transcribe(filename)
    transcription = ''.join([segment.text for segment in segments])
    print(f"[📝] Transcribed Text:\n{transcription}")
    return transcription

def save_note(text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}]\n{text}\n\n")
    print(f"[✅] Note saved to {NOTES_FILE}")

def main():
    audio_data = record_audio()
    wav_file = "temp_audio.wav"
    save_wav(wav_file, audio_data)

    model = WhisperModel(MODEL_SIZE)
    text = transcribe_audio(model, wav_file)
    save_note(text)

if __name__ == "__main__":
    print("2023503523")
    main()
