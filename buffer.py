from dataclasses import dataclass, field
from typing import Dict, List
import json

from .enums import ROTChooser


@dataclass 
class Buffer:
    """Dataclass for encoded data storing as the dict structure"""
    buffer: Dict[str, List[str]] = field(default_factory=lambda: {ROTChooser.ROT47_OPT: [],ROTChooser.ROT13_OPT: []})

    def add_to_buffer(self, text, type):
        """Adds encoded user input to buffer"""
        self.buffer[type].append(text)  

    def show_buffer(self):
        """Prints the data stored in buffer"""
        for key, value in self.buffer.items():
            print(key, value)

    def create_json_from_buffer(self):
        json_object = json.dumps(self.buffer)
        return json_object