from fastapi import FastAPI
from adding_project import creating_dir, ask_chatgpt
from pydantic import BaseModel
from routing import create_new_project
from dotenv import load_dotenv
import os

class PromptForProject(BaseModel):
    prompt: str
    projectname: str

class PromptForAsking(BaseModel):
    prompt: str



app = FastAPI()
load_dotenv()

@app.get("/project/files")

@app.post("/create")
def creating_code(body: PromptForProject):
    dir_path = creating_dir(body.projectname)
    chat = create_new_project(dir_path, body.prompt)
    print(chat)
    return chat

@app.post("/ask")
def asking_chat(body: PromptForAsking):
    return ask_chatgpt(body.prompt)


@app.post("/edit")
def creating_code(body: PromptForProject):
    dir_path = creating_dir(body.projectname)
    chat = create_new_project(dir_path, body.prompt)
    print(chat)
    return chat

