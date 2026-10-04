from openai import OpenAI
from pathlib import Path
import os


client = OpenAI()
mainfolder = os.getnev("MAIN_DIR")


def creating_prompt(project_name, given_prompt, chat_context):
    prompt = f"Name des Projekts: {project_name} Prompt: {given_prompt}"

    response = client.responses.create(
        model = "gpt-5.6-terra",
        input=prompt,
        tools="asig"
        )
    return response

def creating_dir(folder_name):
    folder_path = Path(f"{mainfolder}/{folder_name}")
    folder_path.mkdir(parents=True,exist_ok=True)
    return folder_path

    