from menu import Menu
from enums import ROTChooser, MenuChooser
from rot47 import Rot47
from rot13 import Rot13
from buffer import Buffer

class Manager:
    def __init__(self):
        self.rots = {ROTChooser.ROT47_OPT: Rot47(), ROTChooser.ROT13_OPT: Rot13()}
        self.menu = Menu(
        'Encrypt plain text (ROT47/ROT13)', 
        'Save encrypted texts to file', 
        'Decrypt encrypted text from file (ROT47/ROT13)', 
        'Print encrypted words stored in buffer', 
        'Exit'
        )
        self.options = {MenuChooser.opt_1: self.do_opt1}
        self.buffer = Buffer()
        self.is_running = True

    def execute(self, choice):
        self.options[choice]()

    def start(self):
        while self.is_running:
            self.menu.display()
            choice = self.menu.get_choice()
            self.execute(choice)

    def do_opt1(self):
        # menu
        encoding_choice = self.menu.choose_encoding()
        user_input = self.menu.get_user_input()
        self.rots.get(encoding_choice).encrypt(user_input)
        self.buffer.add_to_buffer(user_input, encoding_choice)
        

    def do_opt_exit(self):
        self.is_running = False




