import ollama

res = ollama.chat(model='phi3:mini', messages=[
  {'role': 'user', 'content': 'write a code two multiply two numbers in python'}
])

print(res['message']['content'])