

def create_file(dir_path, content, file_name):
    file_path = dir_path / file_name
    with open(file_path, "w") as f:
        f.write(content)
    return "sucess"

