class Menu:
    def __init__(self, *args):
        self.menu_list = args

    def display(self):
        for nr, option in enumerate(self.menu_list):
            print(f"{nr + 1}. {option}")

    def get_user_input(self):
        print('Type the text that You want to encrypt: ')
