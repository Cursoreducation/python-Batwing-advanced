import json
from config.file_path import Config

def write_users(users):
    with open(Config.file_path, "w") as file:
        file.write(json.dumps(users))
def get_users():
    file = open(Config.file_path, "r")
    file_data = json.loads(file.read())
    file.close()
    return file_data