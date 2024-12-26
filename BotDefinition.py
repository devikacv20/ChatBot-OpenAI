import openai

openai.api_key = "API_KEY"

class OpenAIBot:
    def __init__(self, engine):
        self.conversation = [{"role": "system", "content": "You are a helpful assistant."}]
        self.engine = engine
    
    def add_message(self, role, content):
        self.conversation.append({"role": role, "content": content})
    
    def generate_response(self, prompt):
        self.add_message("user", prompt)
        try:
            print(f"Conversation: {self.conversation}") 
            
            # Make the API request
            response = openai.ChatCompletion.create(model=self.engine, messages=self.conversation)
            
            # Extracting assistant's response
            assistant_response = response['choices'][0]['message']['content'].strip()
            self.add_message("assistant", assistant_response)
            
            return assistant_response
        except openai.error.OpenAIError as e:
            print(f"OpenAI API Error: {e}")  # More specific OpenAI error handling
        except Exception as e:
            print(f"Unexpected Error: {e}")  # General exception handling
