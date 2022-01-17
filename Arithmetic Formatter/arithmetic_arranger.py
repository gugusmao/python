from ast import IsNot
import sys

def arithmetic_arranger(problems, y=False):
   
    #parameters    
    itens = problems
    tr = y
    cont = 0
    l1 = []
    l2 = []
    l3 = []
    l4 = [] #result

    #chek how many problems were supplied
    if len(itens) > 5:
        print("Error: Too many problems.")
        sys.exit()

    #loop to check the list
    for item in itens: #first loop to split the itens in the list
        sec = item.split()
        for numb in sec: #loop to get every number and parameter to do the math, and config to print in the right order
            numb = numb.strip()
            check = len(numb)
            if (cont-2) <= check: #check what number has the most lengh
                cont = check + 2            
        
        #getting parameters individually and add to the every list
        spac = " "
        spac = (spac*(cont-len(sec[0].strip())))
        
        #check if there is only number on the list
        try:
            sec_0 = int(sec[0].strip())
            sec_1 = str(sec[1].strip())
            sec_2 = int(sec[2].strip())
        except:
            print("Error: Numbers must only contain digits.")
            sys.exit()
        
        #check the max of four digits in width
        if sec_0 > 9999 or sec_2 > 9999:
            print("Error: Numbers cannot be more than four digits.") 
            sys.exit()
        
        #check if the operator is + or -
        if sec_1 != "+" and sec_1 != "-" :
            print("Error: Operator must be '+' or '-'.")
            sys.exit()
        
        line_1 = spac+str(sec_0)   
        
        l1.append(line_1)
        l1.append("    ")
    
        spac_2 = " "
        ger = (cont-1-len(sec[2].strip()))  
        spac_2 = spac_2*ger
        
        line_2 = str(sec_1)+spac_2+str(sec_2) 
        
        l2.append(line_2)
        l2.append("    ")

        
        tra = "-"
        tracado = tra * (cont)
        
        l3.append(tracado)
        l3.append("    ")
        
        #math part
        
        if tr == True:    
            op = {"+": lambda x,y :x+y,
                "-": lambda x,y :x-y}
            
            result = op[sec_1](sec_0,sec_2)
            
            spac_3 = " "
            ger = (cont-len(str(result)))  
            spac_3 = spac_3*ger
            
            line_3 = spac_3+str(result) 
            l4.append(line_3)
            l4.append("    ")
        
   
       
    pr1 = ""
    pr2 = ""
    pr3 = ""
    pr4 = ""

    #sequencial for to print in the right order and vertucally

    for l in l1:
        pr1 = pr1+l
    print(pr1)   

    for l in l2:
        pr2 = pr2+l
    print(pr2)

    for l in l3:
        pr3 = pr3+l
    print(pr3)

    if tr == True: 
        for l in l4:
            pr4 = pr4+l
        print(pr4)
        
    
        