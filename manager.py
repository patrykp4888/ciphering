from menu import Menu
from enums import ROTChooser, MenuChooser
from rot47 import Rot47
from rot13 import Rot13
from buffer import Buffer
from file_handler import FileHandler

class Manager:
    def __init__(self):
        self.rots = {
            ROTChooser.ROT47_OPT: Rot47, 
            ROTChooser.ROT13_OPT: Rot13
            }
        self.menu = Menu(
        'Encrypt plain text (ROT47/ROT13)', 
        'Save encrypted texts to file', 
        'Decrypt encrypted text from file (ROT47/ROT13)', 
        'Print encrypted words stored in buffer', 
        'Exit'
        )
        self.options = {
            MenuChooser.OPT_1: self.do_opt1, 
            MenuChooser.OPT_2: self.do_opt2,
            MenuChooser.OPT_3: self.do_opt3,
            MenuChooser.OPT_4: self.do_opt4,
            MenuChooser.OPT_5: self.do_opt_exit
            }
        self.buffer = Buffer()
        self.file_handler = FileHandler()
        self.is_running = True

    def start(self):
        while self.is_running:
            self.menu.display()
            choice = self.menu.get_choice()
            self.execute(choice)

    def do_opt1(self):
        encoding_choice = self.menu.choose_encoding()
        user_input = self.menu.get_user_input()
        encoded_text = self.rots.get(encoding_choice)().encrypt(user_input)
        self.buffer.add_to_buffer(encoded_text, encoding_choice)

    def do_opt2(self):
        json_object = self.buffer.create_json_from_buffer()
        self.file_handler.save_to_file(json_object)

    def do_opt3(self):
        encoding_choice = str(self.menu.choose_encoding())
        encoded_data = self.file_handler.get_from_file()
        for i in encoded_data[encoding_choice]:
            print(self.rots.get(encoding_choice)().decrypt(i))

    def do_opt4(self):
        self.buffer.show_buffer()

    def do_opt_exit(self):
        self.is_running = False

    def execute(self, choice):
        self.options[choice]()


