def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    
    transport=0
    if(distance_in_kms>0 and distance_in_kms<=3):
        transport=0
    elif(distance_in_kms>3 and distance_in_kms<=6):
        transport=(distance_in_kms-3)*3
    else:
        transport=9+(distance_in_kms-6)*6
    if(food_type=="V" and quantity_ordered>0 and distance_in_kms>0):
        bill_amount=(120*quantity_ordered)+transport
    elif(food_type=="N" and quantity_ordered>0 and distance_in_kms>0):
        bill_amount=(150*quantity_ordered)+transport
    else:
        bill_amount=-1
    return bill_amount

bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)
