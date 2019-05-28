def check_perfect_number(number):
    
    i=1
    divisor=list()
    while i<number:
        if number%i==0:
            divisor.append(i)
            i=i+1
        else:
            i =i+1
    if number== sum(divisor):
        return (True)
     
    else:
        return(False) 
     

def check_perfectno_from_list(no_list):

    perfect=list()
    for i in no_list:
        g=check_perfect_number(i)
        if g==True:
            perfect.append(i)
    if perfect!=[0]:
        return perfect 
   
perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)
