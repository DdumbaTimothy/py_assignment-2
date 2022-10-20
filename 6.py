def is_year_leap():
    year = int(input("Please enter a year"))
    if year %400 ==0 or year %4 ==0:
        print(True,":",year,"is a leap year")
    else:
        print(False, ":",year,"not a leap year")
    
is_year_leap()
