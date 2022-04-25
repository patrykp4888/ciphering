class Menu:
    def __init__(self, *args):
        self.menu_list = args

    def display(self):
        print('-----------------------------------')
        for nr, option in enumerate(self.menu_list):
            print(f"{nr + 1}. {option}")
        print('-----------------------------------')
        self.get_choice()

    def get_choice(self):
        try:
            choice = int(input("Your choice: "))
            return choice
        except ValueError as err:
            print(err)
        
    def get_user_input(self):
        print('Type the text that You want to encrypt: ')
        
    def execute(self, menu_list):
        pass

    def showError(self):
        print("ERROR!")


