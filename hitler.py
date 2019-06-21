from itertools import permutations 
p=list(map(int,input().split())) 
perm = permutations(p)
cost=list()
for i in perm:
     
     sumof=0
     for j in range(2,len(i)-1):
          sumof=sumof+i[j]+i[j+1]
     cost.append(sumof)
print(cost)     
print(min(cost)) 
