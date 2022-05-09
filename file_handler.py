class FileHandler:
    def __init__(self) -> None:
        pass

    def save_to_file(self, data) -> None:
        with open('encoded_texts', 'a') as file:
            file.write(data)

    def get_from_file(self) -> str:
        with open('encoded_texts', 'r') as file:
            data = file.readlines()
        return data

    def create_json(self):
        pass