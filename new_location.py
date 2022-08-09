from Location_Tax_info import Location_Tax_info

class New_Location(Location_Tax_info):
    
    def __init__(self, city, state):
        self.city = city
        self.state = state
        self.new_cli = Location_Tax_info.get_CLI(self)
        self.state_tax = Location_Tax_info.get_St_income_tax(self)