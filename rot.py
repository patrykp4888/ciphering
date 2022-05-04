from abc import ABC


class Rot(ABC):
    def __init__(self):
        pass
    
    def encrypt(self):
        raise NotImplementedError

    def decrypt(self):
        raise NotImplementedError