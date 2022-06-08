import json


class FileHandler:

    def save_to_file(self, data: dict) -> None:
        """Saves json formatted data to file"""
        with open('encoded_texts.json', 'w') as file:
            file.write(data)

    def get_from_file(self) -> dict:
        with open('encoded_texts.json', 'r') as file:
            data = json.load(file)
        return data
