import os
from dotenv import load_dotenv
from groq import Groq

#loading the api key from the .env file
load_dotenv()

client = Groq(api_key=os.environ.get("GROQ-API-KEY"))

messages = [
    {"role": "system", "content": "You are helpful, friendly assistent."}
]

print("Chatbot ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Bye!")
        break

    #adding message of user to conversation history
    messages.append({"role": "user", "content": user_input})

    #Call the model
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        temperature=0.7
    )

    reply = response.choices[0].message.content
    print(f"Bot: {reply}\n")

    #Add model's reply to history too
    messages.append({"role": "assistant", "content": reply})