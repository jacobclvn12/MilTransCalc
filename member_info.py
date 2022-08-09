

class Member_information:
    
    def __init__(self, rank, duty_zip, years_service, HoR_St, total_income):
        self.rank = rank
        self.duty_zip = duty_zip
        self.years_service = years_service
        self.home_of_record = HoR_St
        self.has_dependant = False
        self.total_income = total_income
        # self.net_income = total_income - 'taxes'
        # self.home_of_record_taxes = state_tax[HoR_St]
    
#change dependants from false to true if the member does have dependants, for BAH purposes
    def change_dependant(self):
        self.has_dependant = True
        

