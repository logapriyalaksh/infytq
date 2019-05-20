def sum_all(function, data):
    result_sum=0;
    for w in data:
        if(function(w)):
            result_sum = result_sum+ w
    return result_sum


list_of_nos=[100,200,300,500,1040]

greater =  lambda x:x>10


divide = lambda x : x%10 == 0 and x <101

range_of_values = lambda x : x<=50 and x>=25

print(sum_all(greater,list_of_nos))
print(sum_all(divide,list_of_nos))
print(sum_all(range_of_values,list_of_nos))
