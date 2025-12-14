from openai import OpenAI

client = OpenAI(api_key="PUT_YOUR_API_KEY_HERE")

def ai_agent(task):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI agent that helps with coding and automation."},
            {"role": "user", "content": task}
        ]
    )
    return response.choices[0].message.content


while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    print("Agent:", ai_agent(user_input))
