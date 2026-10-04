from openai import OpenAI
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

last_response_id = None

client = OpenAI()
mainfolder = os.getenv("MAIN_DIR")

def ask_chatgpt(given_prompt):
    response = client.responses.create(
        model = "gpt-5.6-terra",
        input=given_prompt,
        )
    return response.output_text

def creating_prompt(given_prompt, chat_context=[]):
    global last_response_id

    if chat_context:
        given_prompt= chat_context

    response = client.responses.create(
        model = "gpt-5.6-terra",
        input=given_prompt,
        tools=tools,
        previous_response_id=last_response_id
        )
    last_response_id = response.id
    return response

def creating_dir(folder_name):
    folder_path = Path(f"{mainfolder}/{folder_name}")
    folder_path.mkdir(parents=True,exist_ok=True)
    return folder_path

tools = [
    {
        "type": "function",
        "name": "create_file",
        "description": "Creates a new file in a directory with the given content.",
        "parameters": {
            "type": "object",
            "properties": {
                "content": {
                    "type": "string",
                    "description": "Content to write into the file"
                },
                "file_name": {
                    "type": "string",
                    "description": "Name of the file including its extension"
                },
            },
            "required": ["content","file_name"]
        }
    },

{
        "type": "function",
        "name": "get_file_content",
        "description": "Gives back the content of the File",
        "parameters": {
            "type": "object",
            "properties": {
                "file_name": {
                    "type": "string",
                    "description": "Name of the file including its extension"
                },
            },
            "required": ["file_name"]
        }
    },
{
    "type": "function",
    "name": "get_directory_content",
    "description": "Lists all files in the current Directory.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
},
{
    "type": "function",
    "name": "file_edit",
    "description": "allows you to rewrite the file",
    "parameters": {
        "type": "object",
        "properties": {
            "content": {
                "type": "string",
                "description": "The content you wanna write in the file"
            },
              "file_name": {
                        "type": "string",
                        "description": "The file you wanna rewrite"
            }
        },
        "required": ["content, file_name"]
    }
},
{
    "type": "function",
    "name": "creating_dir",
    "description": "allows you to create a directory",
    "parameters": {
        "type": "object",
        "properties": {
            "new_name": {
                "type": "string",
                "description": "The name of the directory you wanna create"
            }
        },
        "required": ["new_name"]
    }
}
]