from .rot import Rot


class Rot13(Rot):
    def __init__(self):
        super().__init__()

    def encrypt(self, text) -> str:
        return self.__do_ciphering(text)

    def decrypt(self, text) -> str:
        return self.__do_ciphering(text)

    def __do_ciphering(self, text):
        x = []
        for i in range(len(text)):
            j = ord(text[i])
            if j >= 33 and j <= 126:
                x.append(chr(33 + ((j + 14) % 94)))
            else:
                x.append(text[i])
        encoded_text = ''.join(x)
        return encoded_text

    