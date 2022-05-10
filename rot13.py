from rot import Rot
import codecs


class Rot13(Rot):
    def __init__(self):
        super().__init__()

    def encrypt(self, text) -> str:
        encoded_text = codecs.encode(text, 'rot_13')
        return encoded_text

    def decrypt(self, text) -> str:
        decoded_text = codecs.decode(text, 'rot_13')
        return decoded_text