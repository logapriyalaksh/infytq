def find_leap_years(given_year):
    i=0
    list_of_leap_years=[]
    while(i<15):
        if(given_year % 400 == 0):
            list_of_leap_years.append(given_year)
            i=i+1
            given_year=given_year+1
        
        elif(given_year % 4 == 0 and given_year%100!=0):
            list_of_leap_years.append(given_year)
            i=i+1
            given_year=given_year+1
        else:
            given_year=given_year+1
        

    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)
