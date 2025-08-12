def chatbot():
    print("Hi! I'm a simple chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            print(f"Bot: You said '{user_input}'")

chatbot()