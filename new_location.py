

from sre_parse import State
from types import CoroutineType


class New_Location:
    
    def __init__(self, city, state):
        self.city = city
        self.state = state
        self.new_cli = None     #find Cost of lIving index in CSV
        self.state_tax = None   #find in CSV