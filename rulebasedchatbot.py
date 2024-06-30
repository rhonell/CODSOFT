def chatbot_response(user_input):
    # Lower case acceptance
    user_input = user_input.lower()

    # Conditional statements based on user inputs 
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm ChatBot, your virtual assistant."
    elif "help" in user_input:
        return "Sure, I'm here to help! What do you need assistance with?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Function for chatbot communication 
def chat():
    print("Welcome to ChatBot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            break

# Start the chatbot communication 
chat()

