from ollama import chat

response = chat(
    model='llama3.2',
    messages=[
        {
            'role': 'user',
            'content': 'What is Oracle PL/SQL?'
        }
    ]
)

print(response['message']['content'])