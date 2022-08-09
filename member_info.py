from Location_Tax_info import Location_Tax_info

class Member_information(Location_Tax_info):
    
    def __init__(self, rank, duty_zip, years_service, HoR_St, total_income):
        self.rank = rank
        self.base_pay = 35000
        self.duty_zip = duty_zip
        self.years_service = years_service
        self.state = HoR_St
        self.has_dependant = False
        self.total_income = total_income
        self.state_tx = self.get_St_income_tax()
        self.fed_tax = self.get_fed_tax(self.base_pay)
        self.net_income = total_income - self.state_tx - self.fed_tax
    
#change dependants from false to true if the member does have dependants, for BAH purposes
    def change_dependant(self):
        self.has_dependant = True
        

