
#Find the number portion in a string and stract transforming into a float type

#String of content
str = 'X-DSPAM-Confidence: 0.8475'

#Finding where the number portion start using ":"
start_pst = (
    str.find(':') + 1
    )

#Slicing the portion number and then removing the 
#spaces while transforming it into a float type
numbers = (
    str[start_pst:]
    )
numbers = float(
    numbers.strip()
    )

#Printing it out 
print(numbers)




