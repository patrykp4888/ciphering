from dataclasses import dataclass, asdict
from typing import Dict, List

from enums import ROTChooser

@dataclass 
class Buffer:
    """Object for data storing"""
    buffer: Dict[str, List[str]] = {ROTChooser.ROT47_OPT: [], ROTChooser.ROT13_OPT: []}

    def add_to_buffer(self, text, type):
        self.buffer[type].append(text)

    # {'rot_13': ['xyz', 'dwad']}
        

    def show_buffer(self):
        print()

        