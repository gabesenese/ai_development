import datetime
import random
import speech_recognition as sr
import pyttsx3
#import ai_model
import pvporcupine
import pyaudio


porcupine = pvporcupine.create(
    access_key='N5DiMLx4CnALiaoZXEcSMLa+qT9+JyR7Tya2EshErRaNH6zynUzaOA==',
    keywords=['picovoice']
)

CHUNK_SIZE = 256
SAMPLE_RATE = porcupine.sample_rate

def get_next_audio_frame():
    audio = audio_stream.read(CHUNK_SIZE, exception_on_overflow=False)
    return audio

pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=SAMPLE_RATE,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=CHUNK_SIZE
)

try:
    while True:
        audio_frame = get_next_audio_frame()
        if len(audio_frame) == 0:
            continue
        
        keyword_index = porcupine.process(audio_frame)
        if keyword_index == 0:
            print("Porcupine detected")
        elif keyword_index == 1:
            pass

except KeyboardInterrupt:
    pass
finally:
    audio_stream.stop_stream()
    audio_stream.close()
    pa.terminate()
    porcupine.delete()

"""

# setup engine for text-to-speech
engine = pyttsx3.init('espeak')
rate = engine.getProperty('rate')
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)




# Get audio from microphone
def MicrophoneAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        r.energy_threshold = 4000
        r.adjust_for_ambient_noise(source)
        r.dynamic_energy_threshold = False
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print("Speech Recognition Error")
        return 'None'
    return query

"""
