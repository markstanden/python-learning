## Week one assignment to create a tip suggestion script

#The given rates by Mattan
options = [0.15, 0.18, 0.20]

#Get the user to provide the cost of the bill
gross_cost_raw = input('How much is the bill? : ')

#if the first character is a dollar symbol, 
#remove the dollar symbol, create float value
#flag the user as american
if gross_cost_raw[0] == '$':
    gross_cost_float = float( gross_cost_raw.replace('$', '', -1) )
    AMERICAN = True
    BRITISH = False

#if the first character is a pound symbol, 
#remove the pound symbol, create float value
#flag the user as british
elif gross_cost_raw[0] == '£':
    gross_cost_float = float( gross_cost_raw.replace('£', '', -1) )
    AMERICAN = False
    BRITISH = True

else:
#nothing to remove, but create float value
    gross_cost_float = float( gross_cost_raw )
    AMERICAN = False
    BRITISH = False

#use the user's (string) input to save messing around
print (f"With a total bill of {gross_cost_raw} the following would be most appropriate:")

#use to alter values inside the list.
#there must be a better way than this, seems longwinded.
counter = 0

if BRITISH:
    #Undertip as standard
    currency = "£"
    for j in options:
        options[counter] *= 0.8
        counter += 1
    
elif AMERICAN:
    #overtip as standard
    currency = "$"
    for j in options:
        options[counter] *= 1.2
        counter += 1
    
else:
    #standard tipping rate
    currency = "‎€"

#Print the options out
option_number = 1
for rate_percentage in options:
    #paste the string together and print to screen.
    print (f'Option {option_number} :\t{ int(rate_percentage * 100) }% \t {currency}{rate_percentage * gross_cost_float:.2f}')
    option_number += 1