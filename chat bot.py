def chatbot():
    print("Chatbot: Hello! I am your simple chatbot. Ask me anything or type 'exit' to end the conversation.")
    
    while True:
        
        user_input = input("You: ").strip().lower()
        
        
        if user_input == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I'm a simple chatbot. You can call me Chatty!")
        elif "weather" in user_input:
            print("Chatbot: I can't check the weather, but it’s always sunny in the world of code!")
        elif "bye" in user_input:
            print("Chatbot: Bye! Come back anytime.")
            break
        elif "help" in user_input:
            print("Chatbot: Sure! I can respond to basic queries like greetings, my name, or how I'm doing. Try asking!")
        elif"tell about current news"or"fengal cyclone" in user_input:
            print("Tamil Nadu is currently on alert due to a developing cyclonic system named Fengal in the Bay of Bengal.")
        else:
            print("Chatbot: I'm sorry, I don't understand that yet. Try asking something else!")


chatbot()
