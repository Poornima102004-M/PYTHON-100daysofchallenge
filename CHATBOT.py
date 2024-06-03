import random

# Define a dictionary of responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you?": ["I'm doing well, thank you!", "I'm good, thanks for asking."],
    "what's your name?": ["I'm just a humble chatbot.", "You can call me ChatBot."],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!"]
}

# Function to generate a response
def respond(message):
    message = message.lower()
    if message in responses:
        return random.choice(responses[message])
    else:
        return "I'm not sure how to respond to that."

# Main function for interacting with the chatbot
def main():
    print("Welcome to the ChatBot!")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye!")
            break
        else:
            print("ChatBot:", respond(user_input))

# Run the main function
if __name__ == "__main__":
    main()
