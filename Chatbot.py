# Simple customer interaction chatbot

# Function to greet the user
def greet():
    print("Chatbot: Hello! How can I assist you today?")

# Function to handle user input and provide a response
def chat():
    while True:
        user_input = input("User: ")
        response = generate_response(user_input)
        print("Chatbot:", response)
        if user_input.lower() == "bye":
            break

# Function to generate a response based on user input
def generate_response(user_input):
    if "order" in user_input.lower():
        return "Sure! Please provide the details of your order."
    elif "payment" in user_input.lower():
        return "We accept various payment methods including credit cards and PayPal."
    elif "shipping" in user_input.lower():
        return "Our standard shipping time is 3-5 business days."
    elif "return" in user_input.lower():
        return "Please refer to our return policy on our website for more information."
    elif "support" in user_input.lower():
        return "Our support team is available 24/7. How can I assist you?"
    elif "thank you" in user_input.lower() or "thanks" in user_input.lower():
        return "You're welcome! If you have any more questions, feel free to ask."
    else:
        return "I'm sorry, I didn't understand. Can you please rephrase your question?"

# Main function to start the chatbot
def main():
    greet()
    chat()

# Start the chatbot
main()
