# I used Groq's Llama model instead of OpenAI because I was using an API
# with available access. The program makes two LLM calls: the first one
# generates two recipes from the ingredients, and the second one uses
# those generated recipes to create a shopping list for the missing
# ingredients.

from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("GROQ_API_KEY was not found.")
    exit()

client = Groq(api_key=api_key)
ingredients = input("Enter comma separated ingredients: ")

recipe_prompt = f"""
I have the following ingredients:
{ingredients}

Generate 2 different recipes using these ingredients.

For each recipe, provide:
1. Recipe name
2. Ingredients
3. Preparation instructions
"""

r1 = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": recipe_prompt
        }
    ]
)

recipes = r1.choices[0].message.content

print("\nGenerated Recipes\n")
print(recipes)

shopping_prompt = f"""
I already have these ingredients:
{ingredients}

Here are the recipes that were generated:

{recipes}

Produce a shopping list for the generated recipes,
excluding the ingredients I already have.

Only include ingredients that I need to buy.
"""

r2 = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": shopping_prompt
        }
    ]
)

shopping_list = r2.choices[0].message.content

print("\nShopping List:\n")
print(shopping_list)