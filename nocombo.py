s="abcab"

l=len(s)
p=list(s[i:j+1] for i in range (len(s)) for j in range(i,len(s)))
print(p,len(p))
count=0
for i in p:
     j=len(i)
     if i[0]==i[j-1]:
          count=count+1
print(count)          
