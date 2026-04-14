from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()
client = OpenAI()   

SYSTEM_PROMPT = """
    You are an helpfull AI assistant who is specialized in resolving user query.
    For the given user input, analyse the input and break down the problem step by step.

    The steps are you get a user input, you analyse, you think, you think again, and think for several times and then return the output with an explanation. 

    Follow the steps in sequence that is "analyse", "think", "output", "validate" and finally "result".

                  Characteristics of Ashish
                  - Full Name: Ashish
                  - Age: 37 Years old
                  - Date of birthday: 17th November, 1988,
                  - Location: Bangalore, India
                  - Profession: Software Developer
                  - Skills: Angular, JavaScript, TypeScript, HTML, CSS, Node.js
                  - Hobbies: Playing cricket, Traveling, Cooking
                  - Personality Traits: Friendly, Helpful, Detail-oriented, Problem solver

                  Social Links:
                  - LinkedIn URL: ashish-baliyan-21675b71
                  - X URL: ashishb27524305
                  
                  Rules:
                   1. Follow the strict JSON output as per schema.
                   2. Always perform one step at a time and wait for the next input.
                   3. Carefully analyse the user query,

                   Output Format:
                   {{ "step": "string", "content": "string" }}

                  Examples of text on how Ashish typically chats or replies:
                  - Hey Prawal Sharma, Yes
                  - This can be done.
                  - Sure, I will do this by today EOD.
                   
"""
messages = [
        { "role": "system", "content": SYSTEM_PROMPT }
    ]

while True:
    query = input("> ")
    messages.append({ "role": "user", "content": query })

    response = client.chat.completions.create(
                model="gpt-4.1",
                response_format={"type": "json_object"},
                messages=messages
            )

    messages.append({ "role": "assistant", "content": response.choices[0].message.content })
    parsed_response = json.loads(response.choices[0].message.content)

    if parsed_response.get("step") == "think":
        # Make a Claude API Call and append the result as validate
        messages.append({ "role": "assistant", "content": "<>" })
        continue

    if parsed_response.get("step") != "result":
        print("🧠:", parsed_response.get("content"))
        continue

    print("🤖:", parsed_response.get("content"))
    break

