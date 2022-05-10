from dataclasses import dataclass, field
from typing import Dict, List

from enums import ROTChooser
import json


@dataclass 
class Buffer:
    """Object for data storing"""
    buffer: Dict[str, List[str]] = field(default_factory=lambda: {ROTChooser.ROT47_OPT: [],ROTChooser.ROT13_OPT: []})

    def add_to_buffer(self, text, type):
        self.buffer[type].append(text)  

    def show_buffer(self):
        for key, value in self.buffer.items():
            print(key, value)

    def create_json_from_buffer(self):
        json_object = json.dumps(self.buffer)
        return json_object