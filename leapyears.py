def leapyears(x):
    if(x%100 == 0):
        y = "The year " + str(x) + " is not a leap year"
        return(y)
    else:
        if(x%4 == 0):
            y = "The year " + str(x) + " is a leap year"
            return(y)
        else:
            y = "The year " + str(x) + " is not a leap year"
            return(y)
