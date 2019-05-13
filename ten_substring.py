def find_ten_substring(num_str):
    ten_substr=[]         #list to store all substring
    for i in range(len(num_str)):
        sum=0
        sub_str=""
        for j in range(i,len(num_str)):
            sum+=int(num_str[j])
            if sum<10:
                sub_str+=num_str[j]
            elif sum==10:
                sub_str+=num_str[j]
                ten_substr.append(sub_str)
#checks if my current index is not my last index as at avoid index out of bound
#error in next line
                if (j!=len(num_str)-1):  
#checks if value at next index is "0". If true, it does not make sum as zero and
#substring as empty, instead continues with same value in next iteration.         
                    if (num_str[j+1]=="0"):
                        continue;
                    else:
                        break;
    return ten_substr; 

num_str="28353002"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
