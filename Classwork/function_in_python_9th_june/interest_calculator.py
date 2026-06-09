#program to calculate simple interest
#function to calculate simple interest
def simple_interest(principal, rate, time):
    #calculate simple interest
    interest=(principal*rate*time)/100
    #return the calculated simple interest 
    return interest
#-------------------------------------------------
#program to calculate compound interest
#function to calculate compound interest
def compound_interest(principal, rate, time):
    #calculate compound interest
    amount=principal*(1+(rate/100))**time
    #return the calculated compound interest 
    return amount   
#-------------------------------------------------