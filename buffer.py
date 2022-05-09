from dataclasses import dataclass, field
from typing import Dict, List

from enums import ROTChooser


@dataclass 
class Buffer:
    """Object for data storing"""
    buffer: Dict[str, List[str]] = field(default_factory=lambda: {ROTChooser.ROT47_OPT: [],ROTChooser.ROT13_OPT: []}) 
    # buffer = {ROTChooser.ROT47_OPT: [], ROTChooser.ROT13_OPT: []}

    def add_to_buffer(self, text, type):
        self.buffer[type].append(text)  

    def show_buffer(self):
        pass

    def prepare_for_saving(self):
        pass