year = 2001
if (year % 4) == 0:
    if (year % 400) == 0:
        print(str(year) +" is a leap year")
    else:
        print(str(year) +" is not a leap year")

else:
    print(str(year) + " is not a leap year")
