import openai

openai.api_key = "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"  # Ensure you have the correct API key

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
