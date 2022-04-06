from menu import Menu

class Manager:
    def __init__(self):
        self.rot47 = Rot47()
        self.rot13 = Rot13()
        self.menu = Menu('Encrypt plain text (ROT47/ROT13)', 'Save encrypted texts to file', 'Decrypt encrypted text from file (ROT47/ROT13)', 'Print encrypted words stored in buffer', 'Exit')

    def start(self):
        self.menu.display()