from ai_functions.writing_file import create_file
from adding_project import creating_prompt
import json
from ai_functions.reading_file import get_file_content
from ai_functions.get_content_of_directory import get_directory_content
from ai_functions.edit_file import file_edit
from ai_functions.create_dir import creating_dir


available_functions = {
    "create_file" : create_file,
    "get_file_content": get_file_content,
    "get_directory_content": get_directory_content,
    "file_edit": file_edit,
    "creating_dir": creating_dir
}



def create_new_project(dir_path, prompt):
    chat_context = []
    while True:
        response = creating_prompt(prompt, chat_context)
        tool_requested = any(item.type == "function_call" for item in response.output)
        if not tool_requested:
            break
        for item in response.output:
            if item.type == "function_call":
                args = json.loads(item.arguments)
                function = available_functions[item.name]
                result = function(dir_path=dir_path,**args)
                chat_context.append({"type": "function_call_output",
                                     "call_id": item.call_id,
                                     "output": json.dumps(result)})
    return chat_context
        
        
