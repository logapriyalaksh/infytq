train_list=[
{"train_no":16453,"name":"Prasanti Express","from":"SBC","to":"BBS","days_of_run":['Mo','We','Th'],"sleeper_fare":600,"ac_fare": 987},
{"train_no":25627,"name":"Karnataka Express","from":"SBC","to":"DEC","days_of_run":['Su','Tu'],"sleeper_fare":1600,"ac_fare": 2500},
{"train_no":22642,"name":"Trivandrum SF Express","from":"VSKP","to":"TVM","days_of_run":['Mo','Tu','We','Th','Fr','Sa'],"sleeper_fare":800,"ac_fare": 1256},
{"train_no":22905,"name":"Okha Howrah Express","from":"ST","to":"KOAA","days_of_run":['We','Sa'],"sleeper_fare":987,"ac_fare": 2879}]

def get_train_name (train_no):
    
    count=0
    for i in train_list:
        for key,value in i.items():
            if key=="train_no" and value==train_no:
                count=1
                return i.get("name")
    if count==0:
        return ("Invalid Train_no")
def get_trains_for_day(day_of_run):
    count=0
    listofnum=[]
    for i in train_list:
        for key,value in i.items():
            if key=="days_of_run" and day_of_run in value:
                count=1
                listofnum.append( i.get("train_no"))
    if count==0:
        return ("Invalid day")
    else:
        return (listofnum)
def get_total_fare(train_no,passenger_dict):
    for i in train_list:
        for key,value in i.items():
            if key=="train_no" and value==train_no:
               
                 sleeper=i.get("sleeper_fare")
                 ac=i.get("ac_fare")
    sleepmem=passenger_dict.get("sleeper") 
    acmem=passenger_dict.get("ac")
    total=acmem*ac + sleepmem*sleeper
    return total
print(get_train_name(25627))
print(get_trains_for_day("Mo"))
print(get_total_fare(22642,{"sleeper":5, "ac":1}))

