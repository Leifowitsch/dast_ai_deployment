def get_file_content(dir_path, file_name):
    file_path = dir_path / file_name
    with open (file_path, "r") as f:
        content = f.read()
    return content

