child_id=[10,20,30,40,50]
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    total_chocolate=sum(chocolates_received)
    
    return total_chocolate
    

def reward_child(child_id_rewarded,extra_chocolates):
    listy=[child_id_rewarded]
    
        
    if(set(listy).issubset(set(child_id))):
        k=child_id.index(child_id_rewarded)
        if(extra_chocolates<1):
            print("Extra chocolates is less than 1")
            
        else:    
            chocolates_received[k]=chocolates_received[k]+extra_chocolates
            
            print(chocolates_received)
    else:
        
        print("Child id is invalid")    
           
    

    

print(calculate_total_chocolates())

reward_child(20,2)
