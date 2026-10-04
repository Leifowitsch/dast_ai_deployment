


def file_edit(dir_path,content, file_name):
    file = dir_path / file_name
    with open(file, "w") as f:
        f.write(content)
    return "success"
