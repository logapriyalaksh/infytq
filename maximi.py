def find_max(num1, num2):
    
    max_num=-1
    sum=0
    i=0
    list=[]
    # Write your logic here
    for i in range(num1,num2):
        if num1<num2:
            if num1//100<1 and num2//100<1:
                digit_sum1=num1%10
                digit_sum2=num2%10
                digit_sum=digit_sum1+digit_sum2
                if  digit_sum%3==0:
                    if num1 %5==0: 
                        list=list.append(num1)
                        num1+=num1
                        max_num=max(list)
                    else:
                        print(-1)
                    
    return max_num
max_num=find_max(10,15)
print(max_num)
