from Location_Tax_info import Location_Tax_info
from current_location import Current_location
from member_info import Member_information
from new_location import New_Location

user = Member_information('E-5', 21108, 7, 'FL')
current_loc = Current_location('Baltimore','MD')
new_loc = New_Location('Phoenix', 'AZ')

def cost_of_living_adjustment():
    prcnt_cli_change = round(((new_loc.new_cli - current_loc.current_cli) / 100),2)
    adjusted_income = user.net_income + (user.net_income * prcnt_cli_change)
    return adjusted_income



#make this adjusting for federal taxes using the function in Location_tax_info
def tax_adjustment():
    cli_adjustment = float(cost_of_living_adjustment())
    current_income_tax = user.fed_tax + (user.total_income * (user.state_tx / 100))
    potential_income_tax = Location_Tax_info.get_fed_tax(cli_adjustment) + (cli_adjustment * (new_loc.state_tax / 100))
    needed_salary = round(cli_adjustment + (potential_income_tax - current_income_tax),2)
    return needed_salary
    
def MilTransCalc():
    cost_of_living_adjustment()
    tax_adjustment()
    print(f'your current yearly income is {user.total_income}, you will need {tax_adjustment()} to move too {new_loc.city}, {new_loc.state}')



MilTransCalc()