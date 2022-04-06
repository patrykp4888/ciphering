class Menu:
    def __init__(self, *args):
        self.menu_list = args

    def display(self):
        for nr, option in enumerate(self.menu_list):
            print(f"{nr + 1}. {option}")