def find_smallest_number(num):
    #start writing your code here
    for value in range(1,1000):
        list=[]
        for n in range(1,value+1):
            if value%n ==0:
                list.append(n)
            
        if len(list) == num:
            return value
            break


num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
