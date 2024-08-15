import nltk
from nltk.chat.util import Chat, reflections

# Define an extended set of patterns and responses
patterns_and_responses = [
    # Greetings
    (r'(hi|hello|hey|greetings)', ['Hello! How can I assist you today?', 'Hi there! What can I do for you?', 'Hey! How can I help you?']),
    
    # Name
    (r'what is your name?', ['I am a chatbot created to assist you.', 'You can call me Chatbot.']),
    
    # Feeling
    (r'how are you?', ['I am just a program, but I am here to help you!', 'I’m doing well, thanks for asking. How can I assist you?']),
    
    # Farewell
    (r'(bye|goodbye|quit|exit)', ['Goodbye! Have a great day!', 'See you later!', 'Bye! If you need any more help, just ask.']),
    
    # Personal Information
    (r'(what|who) (are|is) (you|your name)?', ['I am an advanced chatbot designed to help with various queries.', 'My name is JemChatbot.']),
    
    # Common Questions
    (r'(how|what) (is|are) (you|your) (doing|feeling)?', ['I am here to assist you with any questions you have.', 'I am doing well, thanks for asking.']),
    
    # Jokes
    (r'tell me a joke', ['Why don’t scientists trust atoms? Because they make up everything!', 'Why did the math book look sad? Because it had too many problems.']),
    
    # Weather
    (r'what is the weather like (today|tomorrow)?', ['I am not able to check the weather, but you can use a weather app for the latest updates.', 'I suggest checking a weather website or app for the most accurate information.']),
    
    # Time
    (r'what time is it?', ['I am not able to check the time. You can check your device’s clock for the current time.', 'Please check the time on your device.']),
    
    # Location
    (r'(where|which) (city|place|location) (are|is) you in?', ['I exist in the digital world, so I don’t have a physical location.', 'I am a virtual assistant and don’t have a physical location.']),
    
    # Unknown
    (r'(.*)', ['I am not sure how to respond to that. Can you please ask something else?', 'I am still learning. Could you please rephrase your question?']),
]

# Create the chatbot
chatbot = Chat(patterns_and_responses, reflections)

def chat():
    print("Hi! I am an advanced chatbot. Type 'quit' to end the chat.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() in ['quit', 'exit', 'bye']:
            break

if __name__ == "__main__":
    chat()
