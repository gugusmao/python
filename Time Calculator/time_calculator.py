def add_time(start, end, wd="x"):

    #variables to start
    start = start
    end = end
    wd = wd
    cwd = False
    
    #check if there is AM or PM to the giving variables so it  can be add or not in the function return
    if wd != "x":
        cwd = True

    #finding where it starts and end eache number and outting in some variables
    sip = start.find(":")
    sit = start.find(" ") 

    eip = end.find(":")

    shr = int(start[:sip])

    sminu = int(start[sip+1:sit])

    ehr = int(end[:eip])

    eminu = int(end[(eip+1):])

    #cheking if it is AM or PM start position so I can transform in 24h default hour then adding the end and start number to a variable
    

    sch = start[sit+1:]

    if sch == "PM":
        shr = shr +12

    hresult = shr + ehr

    days = 0

    #Minutes calculation, if there is more than 60 minutes, it adds the respective hour to the adding

    minuresult = sminu + eminu


    if minuresult >= 60:
        x = str(minuresult/60)    
        y = int(x[:(x.find("."))])
        hresult += y
        
        x = float(x) - y
        minuresult = round(x * 60)    


    #hour calculation
    checkampm = False

    while hresult > 12: 
        
        if hresult > 24:  #if the add hour is byond 24h, then it calculate the days that has passed   
            x = hresult/24
            x = str(x)
            days = int(x[:(x.find("."))])
            x = float(x) - days
            x = x * 24                   
            if x > 12:             
                x = x - 12
                checkampm = True 
            else:
                checkampm = False
            if x == 0:
                x += 12
            x += 0.1
            x = str(x)
            hresult = int(x[:(x.find("."))])
            break 
                
        hresult = hresult -12
        if hresult >= 12:
            break
        checkampm = True    

    #getting if the result hour will be AM or PM
    if (hresult >= 12 and sch == "AM") or checkampm == True:
        sch = "PM" 
    elif checkampm == False:
        sch = "AM"
        
    #getting result and the passing in a string


    if minuresult < 10: #adding 0 if the minutes is less than 10
        minuresult = "0"+str(minuresult)
        
    minuresult = str(minuresult)

    fresult = str(hresult)+":"+ minuresult +" "+sch


    wd = wd.capitalize()  #if there is the day name of the week, then this calculate what name will be with the result

    dicw = {"Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4, 
            "Friday":5, "Saturday":6, "Sunday":7}


    if days > 0 and cwd == True:    
        x = dicw[wd]
        x = x + days
        if x <= 7:
            for key, value in dicw.items():
                if value == x:
                    wd = key
        else:
            x = x%7
            for key, value in dicw.items():
                if value == x:
                    wd = key


    if cwd == True:
        fresult = fresult + ", " + wd

    if days > 0:
        if days == 1:
            fresult = fresult+" (next day)"
        else:
            fresult = fresult+" ("+str(days)+" days later)"

    return fresult












