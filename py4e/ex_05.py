#Program that takes how many numbers the users type until he types "done". 
# Then, it prints out the total, count and average of the numbers. 

import numpy as np

#creat variables
list_number = []
key = True
number = 0

#Loop to the user type the numbers
while key == True:
    number = input("Enter a number: ")    
    #Checks if the input is a number then if it's not, it checks if is "done" to 
    # break the loop and get the results
    try:
        number = float(number)
        #print("Is a number")
    except:
        if number == "done":
            #print("Break")
            break
        else:
            print("Invalid input")
            continue
    #Append the number in the list to do the calculations after the loop's break       
    list_number.append(number)
    print(list_number)   
    
#Calculations of the results in the list using fuctions
print("Results")
print("The total is ", sum(list_number))
print("The count is ", len(list_number))
print("The average is ", np.mean(list_number))


