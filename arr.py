arr=list(map(int,input().split()))
l=len(arr)
n=arr[0]
price=list()
for i in range(1,n+1):
     price.append(arr[i])
Q=arr[n+1]
query=list()
for i in range(n+2,l):
     query.append(arr[i])
print(n,price,Q,query)
for i in query:
     M=i
     count=0
     for j in price:
          if M > j:
               count=count+1
     print(count,end=" ")          
          
