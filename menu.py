import encodings
from ssl import Options
from .buffer import Buffer
from .enums import ROTChooser, MenuChooser
from .file_handler import FileHandler


class Menu:
    def __init__(self, *args):
        self.menu_list = args

    def display(self) -> None:
        print('-----------------------------------')
        for nr, option in zip(list(MenuChooser.__dict__.values())[1:], self.menu_list):
            print(f"{nr}. {option}")
        print('-----------------------------------')

    def get_choice(self) -> int:
        try:
            self.choice = int(input('Your choice: '))
            return self.choice
        except:
            print('Invalid choice, try again!')

    def choose_encoding(self) -> int:
        try:
            encoding = int(input(f'Type {ROTChooser.ROT47_OPT} for ROT47\nType {ROTChooser.ROT13_OPT} for ROT13\n')) # TODO
            return encoding
        except :
            print('Invalid choice, try again!')

    def get_user_input(self) -> str:
        user_input = str(input('Type in the text that You want to encrypt:\n'))
        return user_input



