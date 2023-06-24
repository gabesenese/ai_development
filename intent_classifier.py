#from textblob import TextBlob
#import nltk
#from nltk.tokenize import TreebankWordDetokenizer
import json

# Load the existing JSON data from the file
with open('intent.json') as file:
    intents_data = json.load(file)

# Prints all Intents's Tag
for intent in intents_data['intents']:
    print(intent)
    print(intent['tag'])

# Get the tag and intent I want to update or add to
tag_input = input("Which tag would you like to add intents to? " + " > ")
intent_name = tag_input   
intent = None

# Choose between adding an intent in patterns or responses
patterns_input = 'patterns'
responses_input = 'responses'
intent_input = input("Which intent would you like to modify?" + " > ")
if intent not in intents_data:
     print("There is not indent found under " + str(intent_input))

for i in intents_data['intents']:
    if i['tag'] == intent_name:
        intent = i
        break

if intent is None:
    print(f"Intent '{intent_name}' not found in the JSON file.")

# Get User Input
while True:
        user_input = input("Enter user input (or 'q' to quit): ")
        if user_input.lower()  == "q":
             break
        # Check user's input is already in patterns, or check for duplicate
        if user_input in intent['patterns']:
            print("Input is already in patterns Skipping...")
            continue
        elif user_input not in intent['patterns']:
        # Add the user input to the responses
            intent['patterns'].append(user_input)
        print(f"User input '{user_input}' has been appended to the responses for intent '{intent_name}'.")
        # Write the updated JSON data back to the file
        with open('intent.json', 'w') as file:
            json.dump(intents_data, file, indent=4)

