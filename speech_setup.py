import pyttsx3
import speech_recognition as sr
import json
import difflib

#import ai-model
#from scipy.io import wavfile


# Initialize the text-to-speech engine
def initialize_text_to_speech():
    engine = pyttsx3.init('sapi5')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 170)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    return engine

# Initialize the speech recognition engine
def initialize_speech_recognition():
    r = sr.Recognizer()
    return r

# Listen for user's voice input
def listen_for_user_input(r):
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        r.energy_threshold = 4000
        r.adjust_for_ambient_noise(source)
        r.dynamic_energy_threshold = False
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print("User said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Sorry, an error occurred while processing your request. Please try again.")
    return ''

# Process user query based on intents
def process_query(query, engine, intents):
   max_score = 0
   matched_intent = None

   for intent in intents:
       for phrase in intents[intent]['intents']:
        similarity = difflib.SequenceMatcher(None, intent.lower(), query.lower()).ratio()
       if similarity > max_score:
           max_score = similarity
           matched_intent = intent

   if matched_intent:
       execute_intent(matched_intent, intents)

   else:
       respond_default()

       for text in intents['text']:
           if text.lower() in query:
               execute_intent(intent)
               return
           respond_default(engine)

def load_intents(file_path):
    with open(file_path, 'r') as file:
        intents = json.load(file)
    return intents


def execute_intent(intent, engine):
    responses = intents[intent]['responses']
    for response in responses:
        engine.say(response)
    engine.runAndWait()

def respond_default(engine):
    engine.say("I'm sorry, I didn't understand.")
    engine.runAndWait()

def run_ai():
    engine = initialize_text_to_speech()
    r = initialize_speech_recognition()

    while True:
        query = listen_for_user_input(r)
        if query == 'stop':
            break
        process_query(query, engine, intents=intents)

if __name__ == "__main__":
    file_path = 'intents.json'
    intents = load_intents('intents.json')
    run_ai()
