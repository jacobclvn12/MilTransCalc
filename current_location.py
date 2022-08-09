from Location_Tax_info import Location_Tax_info

class Current_location(Location_Tax_info):
    
    def __init__(self, city, state):
        self.city = city
        self.state = state
        self.current_cli = Location_Tax_info.get_CLI(self)
       
