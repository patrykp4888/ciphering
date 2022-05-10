import json


class FileHandler:
    def __init__(self) -> None:
        pass

    def save_to_file(self, data: json) -> None:
        with open('encoded_texts.json', 'w') as file:
            file.write(data)

    def get_from_file(self) -> dict:
        with open('encoded_texts.json', 'r') as file:
            data = json.load(file)
        return data
