#Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out
# the maximum and minimum of the numbers at the end when the user enters “done”. 
# Write the program to store the numbers the user enters in a list and use the max() 
# and min() functions to compute the maximum and minimum numbers after the loop completes. 

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
    
#Calculation of the results in the list using fuctions
print("Results")
print("Maximum: ", max(list_number))
print("Minimum: ", min(list_number))
