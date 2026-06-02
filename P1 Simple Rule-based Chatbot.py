print("ChatBot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ")

    if user == "Hello":
        print("ChatBot: Hello!")

    elif user == "How are you?":
        print("ChatBot: I'm fine!")

    elif user == "What is your name":
        print("ChatBot: I am a simple chatbot.")

    elif user == "bye":
        print("ChatBot: Goodbye!")
        break

    else:
        print("ChatBot: Sorry, I don't understand what you say.")



