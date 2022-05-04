from rot import Rot
import codecs


class Rot47(Rot):
    def __init__(self):
        super().__init__()

    def encrypt(self, text):
        encoded_text = codecs.encode(text, 'rot_47')
        return encoded_text

    def decrypt(self, text):
        decoded_text = codecs.decode(text, 'rot_47')
        return decoded_text