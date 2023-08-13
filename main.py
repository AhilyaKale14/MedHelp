import textbase
from textbase import models
import os
import openai
from typing import List

# Load your OpenAI API key
models.OpenAI.api_key = "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"
# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")


@textbase.chatbot("talking-bot")
def on_message(message_history,SYSTEM_PROMPT):
# # Generate GPT-3.5 Turbo response
    bot_response =  models.openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=SYSTEM_PROMPT + message_history,
    temperature=1,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
    return bot_response["choices"][0]["message"]["content"]
user_input = input("Name:")
SYSTEM_PROMPT = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content":''' Consider yourself as an expert in medical field and provide answer to the asked question as a medical professional.Also in mcq questions just give
      the correct answer with no explanation,for filling the blanks just provide answer for the blank and for comparison provide the comparison in points.Question: ''' +user_input+'''
      ?Answer: '''    }]
message_history=[]
while True:
    user_input = input("User: ")
    # Check for termination condition
    if user_input.lower() in ['quit', 'exit']:
        print("Chatbot: Thank you for trusting us ,Goodbye!")
        break
    message_history.append({"role": "user", "content": user_input})
    bot_response = on_message(SYSTEM_PROMPT, message_history)
    message_history.append({"role": "assistant", "content": bot_response})
    print("Chatbot:",bot_response)
