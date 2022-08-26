from Location_Tax_info import Location_Tax_info
import csv
bah_rates_with = r"2022_BAH_Rates_With.csv"
bah_rates_without = r"2022_BAH_Rates_Without.csv"
zip_mha = r"sorted_zipmha22.csv"


class Member_information(Location_Tax_info):
    
    def __init__(self, rank, duty_zip, years_service, HoR_St, total_income):
        self.mha = None
        self.bah = None
        self.rank = rank
        self.base_pay = 38244
        self.duty_zip = duty_zip
        self.years_service = years_service
        self.state = HoR_St
        self.has_dependant = False
        self.total_income = total_income
        self.state_tx = self.get_St_income_tax()
        self.fed_tax = self.get_fed_tax(self.base_pay)
        self.net_income = self.total_income - ((self.base_pay * (self.state_tx / 100)) + self.fed_tax)
    
#change dependants from false to true if the member does have dependants, for BAH purposes
    def change_dependant(self):
        self.has_dependant = True
    
    def get_bah(self):
        with open(zip_mha) as mha:
                reader = csv.DictReader(mha)
                for line in reader:
                    if self.duty_zip == line['zipcode']:
                        self.mha = line['mha']
                        return self.mha
        if self.has_dependant == True:
            with open(bah_rates_with) as bah_with:
                    reader = csv.DictReader(bah_with)
                    for line in reader:
                        if self.mha == line['mha']:
                            self.bah = float(line[self.rank]) * 12
                            return self.bah
        print(self.mha)
        print(self.bah)



        

