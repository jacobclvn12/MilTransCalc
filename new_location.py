import csv
path = r'/home/jmcolvin/Desktop/MilTransCalc/cost_living_index.csv'


class New_Location:
    
    def __init__(self, city, state):
        self.city = city
        self.state = state
        self.new_cli = 0
        self.state_tax = None   #find in CSV
        with open(path) as cost_living_index:
            reader = csv.DictReader(cost_living_index)
            for line in reader:
                if self.city == line['City'] and self.state == line['State']:
                    self.new_cli = int(line['Index'])