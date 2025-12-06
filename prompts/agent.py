import openai
import sys
import json

def load_prompt():
    with open("prompts/accounting_prompt.txt", "r") as f:
        return f.read()
def generate_journal(problem):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = load_prompt() + "\n\nTransaction:\n" + problem

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
        ]
    )
    return response.choices[0].message["content"]

if _name_ == "_main_":
    raw_input = sys.argv[1]  # input dari GitHub Action
    result = generate_journal(raw_input)

    with open("output.md", "w") as f:
        f.write(result)

    print("Generated journal saved to output.md")
