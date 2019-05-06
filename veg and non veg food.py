def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    N=150
    V=120
    #write your logic here
    if food_type=="N":
        if distance_in_kms==3:
            print(N*quantity_ordered)
                
        elif distance_in_kms==4:
                cost=3
                print("bill_amount:",N*quantity_ordered*cost)
        elif distance_in_kms==5:
                cost=3*2
                print("bill_amount:",N*quantity_ordered*cost)
        elif distance_in_kms==6: 
                cost=3*3
                print("bill_amount:",N*quantity_ordered*cost)
        else:
            while distance_in_kms>6:
                cost=distance_in_kms+6
                print("bill_amount:",N*quantity_ordered*cost)

    elif food_type=="V":
        if distance_in_kms==3:
            print(N*quantity_ordered)
                
        elif distance_in_kms==4:
                cost=3
                print("bill_amount:",V*quantity_ordered*cost)
        elif distance_in_kms==5:
                cost=3*2
                print("bill_amount:",V*quantity_ordered*cost)
        elif distance_in_kms==6: 
                cost=3*3
                print("bill_amount:",V*quantity_ordered*cost)
        else:
           while distance_in_kms>6:
               cost=distance_in_kms+6
               print("bill_amount:",V*quantity_ordered*cost)

    else:
        print(-1)
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)
