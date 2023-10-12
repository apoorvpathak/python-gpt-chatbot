import openai

openai.api_key = "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"


def chat(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
user_name = input("Please assign a 'name' attribute to your real-world self:")
if __name__ == "__main__":
    while True:
        user_input = input(user_name + ":")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat(user_input)
        print("chatbot: ", response)