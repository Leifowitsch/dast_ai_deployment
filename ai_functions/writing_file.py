from adding_project import creating_dir
from pathlib import Path

def create_file(projectname, content):
    with open("mainpath/"+ projectname, "w") as f:
        f.write(content)

