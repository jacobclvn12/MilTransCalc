# MilTransCalc
Calculate needed income when transitioning out of military to a new city

It takes in a Military members Information, using the Member_info.py, this is needed for getting the amount they currently make, and approximatly pay in taxes (military can be stationed in a state with state taxes, but their Home of Record is a state without, meaning they don't pay state taxes.)
it takes in the cit,state they currently live in to get the average cost of living for that using  AdvisorSmith Cost of Living Index. this pulls housing costs, food, and average health care cost into one index.
the member then sets what city,state they are interested in moving too, and it does the same for that location.
the runner takes both locations and compares the cost of living index, then looks at what your taxes would change and tells the military member how much they would need to earn to match what they currently make.

example: I was E5, stationed at Ft Meade, but my home of record was fl. total income with housing allowance was like 75k, but housing allowance is not taxed, so my taxable income was only like 35k. only paying fed taxes since florida doesnt have state income tax. the app looks up what my BAH rate and pay should be off my duty station zipcode, rank, and years of service.

to stay in baltimore it first looks at the cost of living, doesn't change much since the location didn't change, but then for taxes it then takes into account that I jump a few tax brackets to go from taxable income of 35k, to 75k. and then includes State taxes as well (I just took the middle of states with a state tax range). 

so even to stay where I was I still needed higher income to account for tax changes and home of record changes. the App does all that for you.
