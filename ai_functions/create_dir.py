from pathlib import Path

def creating_dir(dir_path, new_name):
    new_dir = dir_path / new_name
    new_dir.mkdir(parents=True, exist_ok=True)
    return "success"