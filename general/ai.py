import openai
openai.api_key = 'sk-proj-k3XoBnJ1BY7Y8OmmGN5eT3BlbkFJV3mrmuUXj55GCqlZYZ0Q'
messages = [ {"role": "system", "content":"You are a intelligent assistant."} ]

message = input("User : ")
if message:
    messages.append(
        {"role": "user", "content": message},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    answer = chat.choices[0].message.content
    print(f"ChatGPT: {answer}")
    messages.append({"role": "assistant", "content": answer})