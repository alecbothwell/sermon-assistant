# main.py
import recorder
import transcriber
import time

recorded_files = []  # List to store recorded filenames

print('Recording and Transcribing')

while True:
    # Record audio
    recorded_file = recorder.record_audio()
    recorded_files.append(recorded_file)
    print(f"Saved {recorded_file}")
    
    # Transcribe the latest audio
    transcriber.transcribe_latest_audio(recorded_file, recorded_files)
    
    time.sleep(1)  # Pause for 1 second before the next loop iteration
