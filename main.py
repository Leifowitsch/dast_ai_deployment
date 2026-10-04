import fastapi
from creating import creating_prompt
from pydantic import BaseModel

class PrompForProject(BaseModel):
    prompt: str



app = fastapi()

@app.get("/project/files")

@app.get("/create")
def creating_code():
    creating_prompt(prompt)


