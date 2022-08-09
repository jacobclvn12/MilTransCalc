from current_location import Current_location
from member_info import Member_information
from new_location import New_Location

Jake = Member_information('E5', 21108, 6, 'FL', 85000)
current_loc = Current_location('Denver','CO')
new_loc = New_Location('Baltimore', 'MD')

def cost_of_living_adjustment():
    prcnt_cli_change = round(((new_loc.new_cli - current_loc.current_cli) / 100),2)
    adjusted_income = Jake.total_income + (Jake.total_income * prcnt_cli_change)
    return adjusted_income

print(cost_of_living_adjustment())

