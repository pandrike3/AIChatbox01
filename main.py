import openai

 
openai.api_key = "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"

def chat_with_gpt(prompt):
     
    response = openai.ChatCompletion.create(
        model="gpt-4",   
        messages=[{"role": "user", "content": prompt}]   
    )

   
    return response.choices[0].message.content.strip()

 
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
