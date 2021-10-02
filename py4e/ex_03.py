"""This script how many hours and rate you pass to calculate the pay you 
get and if you worked above 40 hours then you get 1,5 times the houry rate."""

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Error, please enter num1eric input") 
    quit() 

    
pay = hours*rate

#check and calculate 1.5 times the pay if worked hours is above 40
if (hours > 40):
    #print("Overtime")
    pay = pay + ((hours-40) * (rate*0.5))
#else:
    #print("Regular")    

print('Pay: ', pay)