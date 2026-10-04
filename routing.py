from ai_functions.writing_file import create_file
from adding_project import creating_prompt
import json

tools = ""
available_functions = {
    "create_file" : create_file
}

def create_new_project(projectname, prompt):
    chat_context = []
    while True:
        response = creating_prompt(projectname, prompt, chat_context)
        tool_requested = any(item.type == "function_call" for item in response)
        if not tool_requested:
            break
        for item in response:
            if item.type == "function_call":
                args = json.loads(item.arguments)
                function = available_functions[item.name]
                result = function(**args)
                chat_context.append(result)
        






    create_file()