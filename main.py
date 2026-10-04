import fastapi
from adding_project import creating_prompt, creating_dir
from pydantic import BaseModel
from routing import create_new_project
class PromptForProject(BaseModel):
    prompt: str
    projectname: str



app = fastapi()

@app.get("/project/files")

@app.get("/create")
def creating_code(body: PromptForProject):
    folder_path = creating_dir(body.projectname)
    create_new_project(body.projectname)




