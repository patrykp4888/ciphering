import encodings
from buffer import Buffer
from enums import ROTChooser, MenuChooser
from file_handler import FileHandler

class Menu:
    def __init__(self, *args):
        self.menu_list = args

    def display(self) -> None:
        print('elo')
        # print('-----------------------------------')
        # for nr, option in zip(MenuChooser.__dict__.keys(), self.menu_list): #zip(manager.options.keys(), self.menu_list)
        #     print(f"{nr + 1}. {option}")
        # print('-----------------------------------')

    def get_choice(self) -> int:
        try:
            self.choice = int(input('Your choice: '))
            return self.choice
        except ValueError as err:
            print(err)

    def choose_encoding(self) -> int:
        encoding = int(input(f'Type {ROTChooser.ROT47_OPT} for ROT47\n Type {ROTChooser.ROT13_OPT} for ROT13\n'))
        return encoding

    def get_user_input(self) -> str:
        user_input = str(input('Type the text that You want to encrypt:' ))
        return user_input



