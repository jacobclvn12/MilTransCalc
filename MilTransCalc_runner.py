from current_location import Current_location
from member_info import Member_information
from new_location import New_Location

user = Member_information('E5', 21108, 6, 'CA', 85000)
current_loc = Current_location('Denver','CO')
new_loc = New_Location('Baltimore', 'MD')

def cost_of_living_adjustment():
    prcnt_cli_change = round(((new_loc.new_cli - current_loc.current_cli) / 100),2)
    adjusted_income = user.net_income + (user.net_income * prcnt_cli_change)
    return adjusted_income



#make this adjusting for federal taxes using the function in Location_tax_info
def tax_adjustment():
    st_tx_dif = ((new_loc.state_tax - user.get_St_income_tax())/100)
    cli_adjustment = cost_of_living_adjustment()
    post_tx_income = float(cli_adjustment) - (float(cli_adjustment) * st_tx_dif)
    return post_tx_income

print(user.federal_tax)

