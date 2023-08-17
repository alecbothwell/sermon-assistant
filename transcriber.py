# transcriber.py
import whisper
import os
import glob
import config

def transcribe_latest_audio(model, transcribed_list):
    # Get most recent wav recording in the recordings directory
    recordings_dir = os.path.join('recordings', '*')
    files = sorted(glob.iglob(recordings_dir), key=os.path.getctime, reverse=True)
    
    if len(files) < 1:
        return
    
    latest_recording = files[0]

    if os.path.exists(latest_recording) and latest_recording not in transcribed_list:
        print(latest_recording)
        audio = whisper.load_audio(latest_recording)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        options = whisper.DecodingOptions(language='en', fp16=False)

        result = whisper.decode(model, mel, options)

        if result.no_speech_prob < 0.5:
            print(result.text)

            # Append text to transcript file
            with open(config.TRANSCRIPT_FILE, 'a') as f:
                f.write(result.text + '\n')
        
            # Save list of transcribed recordings
            transcribed_list.append(latest_recording)
