import csv
path = r'/home/jmcolvin/Desktop/MilTransCalc/cost_living_index.csv'

class Current_location:
    
    def __init__(self, city, state):
        self.city = city
        self.state = state
        self.current_cli = 0
        with open(path) as cost_living_index:
            reader = csv.DictReader(cost_living_index)
            for line in reader:
                if self.city == line['City'] and self.state == line['State']:
                    self.current_cli = int(line['Index'])

current_city = Current_location('Baltimore', 'MD')

print(current_city.current_cli)