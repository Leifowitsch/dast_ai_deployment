from pathlib import Path

def get_directory_content(dir_path):
    directory = Path(dir_path)
    directory_content = []
    for item in directory.iterdir():
        directory_content.append(str(item))
    return directory_content
    