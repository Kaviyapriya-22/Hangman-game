import nltk
import random
import string
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize


nltk.download('punkt')


pairs = [
    [r"(hi|hello|hey)", ["Hello!", "Hey there!", "Hi, how can I help you?"]],
    [r"how are you(.*)", ["I'm doing great, thank you! How about you?", "I'm fine, thanks for asking!"]],
    [r"what is your name(.*)", ["I am a chatbot created for you.", "You can call me ChatGPT-lite!"]],
    [r"(.*) your purpose(.*)", ["I exist to assist you with any basic queries!", "I'm here to chat and help."]],
    [r"quit", ["Goodbye! Have a great day!", "Bye, take care!"]],
    [r"(.*)", ["I'm sorry, I didn't understand that.", "Could you rephrase that, please?"]]
]
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

def chatbot():
    print("Chatbot: Hello! Type 'quit' to end the chat.")
    chat = Chat(pairs, reflections)  
    chat.converse()

if __name__ == "__main__":
    chatbot()
