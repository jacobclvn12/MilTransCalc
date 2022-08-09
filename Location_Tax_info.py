import csv
from os import TMP_MAX
cli_csv = r'C:\Users\Jacob\Documents\VS Code\MilTransCalc\cost_living_index.csv'
st_income_tax_csv = r'C:\Users\Jacob\Documents\VS Code\MilTransCalc\st_inc_tx.csv'
class Location_Tax_info:
    
    def get_CLI(self):
        with open(cli_csv) as cost_living_index:
                reader = csv.DictReader(cost_living_index)
                for line in reader:
                    if self.city == line['City'] and self.state == line['State']:
                        index = float(line['Index'])
                        return index  

    def get_St_income_tax(self):
        with open(st_income_tax_csv) as st_income_tx:
                reader = csv.DictReader(st_income_tx)
                for line in reader:
                    if self.state == line['State']:
                        tax_rate = float(line['Tax rates'])
                        return tax_rate

    def get_fed_tax(self,income):
        tax_rate = 0
        net_income = 0
        if income >= 0 and income <=10257:
            tax_rate = .1
        elif income >= 10276 <= 41775:
            tax_rate = .12
        elif income >= 41776 <= 89075:
            tax_rate = .22
        elif income >= 89076 <= 170050:
            tax_rate = .24
        elif income >= 170051 <= 215950:
            tax_rate = .32
        elif income >= 215951 <= 539900:
            tax_rate = .35
        elif income >= 539901:
            tax_rate = .37
        tax_owed = (income * tax_rate)
        return tax_owed

    
