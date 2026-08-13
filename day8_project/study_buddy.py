# I tested the Study Buddy with two different temperature values, 0.1 and 0.9.
# With 0.1, the response was more focused and predictable, while with 0.9,
# the response used a different and more creative analogy. The main idea
# of the explanation stayed the same, but the wording and examples changed.
# This helped me see how temperature affects the creativity and variety of
# an LLM's responses.

from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("GROQ_API_KEY was not found.")
    exit()

client = Groq(api_key=api_key)
system_prompt = """
You are a friendly Python Study Buddy.
You help students understand Python programming concepts.
Explain concepts in simple language and give examples when useful.
Do not just give the answer; try to help the student understand the concept.
"""
messages = [
    {
        "role": "system",
        "content": system_prompt
    }
]

print("Python Study Buddy:")
print("Ask questions about Python.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Study Buddy: Good luck with your studies!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.9
    )

    answer = response.choices[0].message.content

    print("\nStudy Buddy:", answer, "\n")

    messages.append({
        "role": "assistant",
        "content": answer
    })