import csv
path = r'C:\Users\Jacob\Documents\VS Code\MilTransCalc\cost_living_index.csv'

class Location_Tax_info:
    
    def get_CLI(self):
        with open(path) as cost_living_index:
                reader = csv.DictReader(cost_living_index)
                for line in reader:
                    if self.city == line['City'] and self.state == line['State']:
                        index = float(line['Index'])
                        return index                      