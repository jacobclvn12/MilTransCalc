from Location_Tax_info import Location_Tax_info
import pymongo

#connect to MongoDB Database and pulls needed Collections
myclient = pymongo.MongoClient("mongodb+srv://jacobclvn12:Ep2f47ype@miltranscalc.iwijrtc.mongodb.net")
mydb = myclient["MilPayDataBase"]
mha_col = mydb['MHA_Zipcode_lookup']
bw_col = mydb['bah_with_rates']
bwo_col = mydb['bah_without_rates']
mil_pay = mydb['military_pay_rates']


class Member_information(Location_Tax_info):
    
    def __init__(self, rank, duty_zip, years_service, HoR_St):
        self.rank = rank
        self.duty_zip = duty_zip
        self.mha = self.get_mha()
        self.has_dependant = False
        self.bah = int(self.get_bah())
        self.years_service = self.generalize_YoS(years_service)
        self.state = HoR_St
        self.base_pay = self.get_yearly_base_pay()
        self.state_tx = int(self.get_St_income_tax())
        self.fed_tax = int(self.get_fed_tax(self.base_pay))
    #chages the dependant status of the user, which changes bah amount, then reruns functions affected by the change
    def change_dependant(self):
        self.has_dependant = True
        self.bah = self.get_bah()
        self.total_income = self.total_income_fn()
        self.net_income = self.net_income_fn()

    #Mil pay is based of years of service, based on every other, with execption to first few years, this changes the odds to the evens when needed
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
            self.years_service = self.years_service
            return self.years_service
    #pulls the years of service and rank to find the base pay for the user
    def get_yearly_base_pay(self):
        yos = self.generalize_YoS(self.years_service)
        mquery = {'Rank': self.rank}
        mydoc = mil_pay.find(mquery)
        for x in mydoc:
           base_pay = x[str(yos)]
           self.base_pay = int(base_pay) * 12
        return self.base_pay
    #getting a users BAH Rates is dependant on their Duty station zipcode, this uses more general MHAs to compile all zipcodes
    def get_mha(self):
        mquery = {'zipcode': str(self.duty_zip)}
        mydoc = mha_col.find(mquery)
        for x in mydoc:
            mha = x['mha']
            self.mha = x['mha']
        return self.mha

#finds bah if they have a dependant, sub func of get_bah()
    def bah_with_dep(self):
        mquery = {'mha': str(self.mha)}
        mydoc= bw_col.find(mquery)
        for x in mydoc:
            bah = x[self.rank]
            self.bah = int(bah) * 12
        return self.bah

#finds bah if they don't have a dependant, sub func of get_bah()
    def bah_wo_dep(self):
        mquery = {'mha': str(self.mha)}
        mydoc= bwo_col.find(mquery)
        for x in mydoc:
            bah = x[self.rank]
            self.bah = int(bah) * 12
        return self.bah
#checks the dependant status of the user, and runs the correct bah lookup
    def get_bah(self):
        if self.has_dependant:
            self.bah = self.bah_with_dep()
        else:
            self.bah = self.bah_wo_dep()
        return self.bah
#adds base pay with bah and bas
    def total_income_fn(self):
        self.total_income = self.base_pay + self.bah + 4638
        return self.total_income
#takes into account taxes and removes them from total income
    def net_income_fn(self):
        total_income = self.total_income_fn()

        self.net_income = int(total_income - ((self.base_pay * (self.state_tx / 100)) + self.fed_tax))
        return self.net_income











user = Member_information('E-5', 21108, 7, 'FL')

print(user.bah)
print(user.base_pay)
user.total_income_fn()
print(user.total_income)
user.change_dependant()
print(user.has_dependant)
print(user.bah)
print(user.total_income)


