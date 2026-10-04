from openai import OpenAI

client = OpenAI()


def creating_prompt(prompt):
    prompt = "safsa"

    response = client.responses.create(
        model = "gpt-5.6-terra",
        input=prompt
        )