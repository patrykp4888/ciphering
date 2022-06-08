from abc import ABC, abstractmethod


class Rot(ABC):
    
    @abstractmethod
    def encrypt(self):
        raise NotImplementedError

    @abstractmethod
    def decrypt(self):
        raise NotImplementedError