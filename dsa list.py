def merge_list(list1, list2):
    merged_data=""
    #write your logic here
    list2.reverse()
    newlist=[]
    for i in range (0,len(list1)):
        if(list2[i]!=None and list1[i]!=None):
            newlist.append(list1[i]+list2[i])
        elif(list1[i]!=None and list2[i]==None):
            newlist.append(list1[i])
        elif(list2[i]!=None and list1[i]==None):
            newlist.append(list2[i])    
    for e in newlist:
        merged_data+=e+" "
            
        
    return merged_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data.strip())
