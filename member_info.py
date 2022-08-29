from Location_Tax_info import Location_Tax_info
import csv
pay_chart_csv = r'data\Military_Pay.csv'
mha_csv = r"data\mha.csv"
bah_without = r'data/bah_rate_without.csv'
bah_with = r'data/bah_rate_with.csv'



class Member_information(Location_Tax_info):
    
    def __init__(self, rank, duty_zip, years_service, HoR_St):
        self.rank = rank
        self.mha = None
        self.duty_zip = duty_zip
        self.has_dependant = False
        self.bah = self.get_bah()
        self.years_service = self.generalize_YoS(years_service)
        self.state = HoR_St
        self.base_pay = self.get_yearly_base_pay()
        self.total_income = self.base_pay + self.bah +  4638
        self.state_tx = self.get_St_income_tax()
        self.fed_tax = self.get_fed_tax(self.base_pay)
        self.net_income = self.total_income - ((self.base_pay * (self.state_tx / 100)) + self.fed_tax)
    
#change dependants from false to true if the member does have dependants, for BAH purposes

    
    def generalize_YoS(self,years_service):
        if years_service < 2:
            self.years_service = '<2'
            return self.years_service
        elif years_service >= 2 and years_service < 3:
            self.years_service = 2
            return self.years_service
        elif years_service >= 3 and years_service < 4:
            self.years_service = 3
            return years_service
        elif years_service >= 4 and years_service < 6:
            self.years_service = 4
            return self.years_service
        elif years_service >= 6 and years_service < 8:
            self.years_service = 6
            return self.years_service
        elif years_service >= 8 and years_service < 10:
            self.years_service = 8
            return self.years_service
        elif years_service >= 10 and years_service < 12:
            self.years_service = 10
            return self.years_service
        elif years_service >= 12 and years_service < 14:
            self.years_service = 12
            return self.years_service
        elif years_service >= 14 and years_service < 16:
            self.years_service = 14
            return self.years_service
        elif years_service >= 16 and years_service < 18:
            self.years_service = 16
            return self.years_service
        elif years_service >= 18 and years_service < 20:
            self.years_service = 18
            return self.years_service
        elif years_service >= 20 and years_service < 22:
            self.years_service = 20
            return self.years_service

    def get_yearly_base_pay(self):
        with open(pay_chart_csv) as pay_chart:
                        reader = csv.DictReader(pay_chart)
                        for line in reader:
                            if self.rank == line['Rank']:
                                income_str = line[str(self.years_service)]
                                self.base_pay = int(income_str)*12
                                return self.base_pay
    
    def bah_with_dep(self):
        with open(bah_with) as bah_w:
            reader_with = csv.DictReader(bah_w)
            for line in reader_with:
                if self.mha == line['mha']:
                    user_bah_w = line[self.rank]
                    self.bah = int(user_bah_w)*12
                    return self.bah

    def bah_wo_dep(self):
        with open(bah_without) as bah_wo:
            reader_wo = csv.DictReader(bah_wo)
            for line in reader_wo:
                if self.mha == line['mha']:
                    user_bah = line[self.rank]
                    self.bah = int(user_bah)*12
                    return self.bah

    def get_bah(self):
        with open(mha_csv) as mha:
            reader = csv.DictReader(mha)
            for line in reader:
                if str(self.duty_zip) == line['zipcode']:
                    self.mha = line['mha']        
                    if self.has_dependant == True:
                        continue
                    return self.bah_wo_dep()

    def change_dependant(self):
        self.has_dependant = True
        self.bah_with_dep()

