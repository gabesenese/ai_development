import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Embedding, LSTM, Dense


"""


To Do
-====-

- Setup a base foundation and framework for ai with machine learning, NLU
- Use JSON as intents for AI to help with word and speech categorization and sentiment analysis




"""


# AI model
def load_intent_data(file_path):
    with open(file_path, 'r') as file:
        intents = json.load(file)

    input_texts, intent_responses = [], []
    for intent in intents["intents"]:
        for text in intent["text"]:
            input_texts.append(text)
            for response in intent["responses"]:
                intent_responses.append(response)

    preprocessed_input_texts = input_texts
    preprocessed_intent_responses = intent_responses

    return preprocessed_input_texts, preprocessed_intent_responses


# Define the AI model architecture
vocab_size = 1000
embedding_dim = 100
max_sequence_length = 50
num_classes = 2

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(
        vocab_size, embedding_dim, input_length=max_sequence_length),
    tf.keras.layers.LSTM(64, return_sequences=True),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])


# Train the AI model
def train_model(model, X_train, y_train, batch_size=32):
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, batch_size=batch_size)


# Load and preprocess the intent data
intent_data_file = 'intent.json'
X_train, y_train = load_intent_data(intent_data_file)

# Convert the training data to appropriate formats
X_train = np.array(X_train)
y_train = np.array(y_train)

# Save the trained model
model.save('trained_model.h5')

# Load the pre-trained model
trained_model = keras.models.load_model('trained_model.h5', compile=False)


