
from BotDefinition import OpenAIBot
engine = "gpt-3.5-turbo"  
# engine = "gpt-3.5-turbo-16k"
# engine = "gpt-4"

chatbot = OpenAIBot(engine)

while True:
    prompt = input("You: ")
    if prompt.upper() == 'END CHAT':
        print("Ending chat.")
        break

    response = chatbot.generate_response(prompt)
    if response:
        print(f"Bot: {response}")
    else:
        print("Bot could not generate a response.")
