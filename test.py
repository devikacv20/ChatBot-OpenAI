import openai

openai.api_key = "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"

try:
    response = openai.Model.list()
    print("API is working!")
    print(response)
except Exception as e:
    print("Error:", e)
