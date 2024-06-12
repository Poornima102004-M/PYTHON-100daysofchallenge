import random

def get_response(user_input):
    responses = [
        "Interesting, tell me more.",
        "I'm not sure I understand. Can you elaborate?",
        "That's fascinating!",
        "I see. What do you think about it?",
        "Hmm, let me think about that for a moment.",
        "Why do you say that?",
        "That's a good point.",
        "I'm not sure I agree. Let's discuss it further.",
    ]
    return random.choice(responses)

def main():
    print("Welcome to the Random Chatbot!")
    print("You can start chatting. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").strip().lower()
        if user_input == 'exit':
            print("Goodbye!")
            break
        else:
            response = get_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()
