# recorder.py
import sounddevice as sd
from scipy.io import wavfile
import datetime
import numpy as np
import re

freq = 44100
duration = 5  # in seconds

def sanitize_filename(filename):
    return re.sub(r'[\/:*?"<>|]', '_', filename)

def record_audio():
    ts = datetime.datetime.now()
    filename = ts.strftime("%Y-%m-%d-%H_%M_%S")
    compFile = "./recordings/" + sanitize_filename(filename) + ".wav"

    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1, dtype='int16')
    sd.wait()

    wavfile.write(compFile, freq, recording.astype(np.int16))
    return compFile