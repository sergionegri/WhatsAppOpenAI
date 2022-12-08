import os
import openai
import json

# TODO load API key from an environment variable or secret management service
#openai.api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = 'XXXXX'

input='List 10 movies that are similar to interstellar, memento and tenet'

response = openai.Completion.create(model="text-davinci-003", 
                                    prompt=input, 
                                    temperature=0.5,
                                    max_tokens=250,
                                    top_p=1.0,
                                    frequency_penalty=0.0,
                                    presence_penalty=0.0
                                   )

print(response["choices"][0]["text"])