def month_Calender(year , month):        
    
    all_Months = {"jan":31 , "mar":31 , "apr":30 , "may":31 , "jun":30 , "jul":31 , "aug":31 , "sep":30 , "oct":31 , "nov":30 , "dec":31}
    
    if month == "feb":
        if ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
            print(f"February {year} has 29 days.")
        else:
            print(f"February {year} has 28 days.")
    else:
        for i in all_Months:
            if (month == i):
                print(f"{month} {year} has {all_Months[i]} days")
    
    

yr = int(input("Enter a year: "))
mth = input("Enter the name of a month:")
month_Calender(yr,mth)