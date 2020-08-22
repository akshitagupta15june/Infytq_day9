    #PF-Prac-17
train_list=[{'train_no': 23492, 'days_of_run': ['Su', 'Mo', 'We'], 'name': 'Tuticorin Express', 'sleeper_fare': 450, 'to': 'TUT', 'from': 'MYS', 'ac_fare': 780}, {'train_no': 45200, 'days_of_run': ['Mo', 'Fr'], 'name': 'Kaveri Express', 'sleeper_fare': 700, 'to': 'CHN', 'from': 'MYS', 'ac_fare': 1200}, {'train_no': 12093, 'days_of_run': ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'], 'name': 'Lokmanya Express', 'sleeper_fare': 720, 'to': 'LOK', 'from': 'CBE', 'ac_fare': 1340}, {'train_no': 67234, 'days_of_run': ['Th', 'Fr', 'Sa'], 'name': 'Poorna Express', 'sleeper_fare': 987, 'to': 'PUN', 'from': 'ERN', 'ac_fare': 2879}]
def get_train_name (train_no):
    for i in train_list:
        for j in i:
            if i[j]==train_no:
                return i
    return "Invalid Train_no"
        #start writing your code here
        
def get_trains_for_day(day_of_run):
        #start writing your code here
    list=[]
    for i in  train_list:
        for j in i: 
            n= i['days_of_run']
            if day_of_run in n:
                if i['train_no'] not in list:
                    list.append(i['train_no'])
    if list == []:
        return "Invalid day"
    return list       
def get_total_fare(train_no,passenger_dict):
        #start writing your code here
    n=0
    for i in train_list:
        for j in i:
            if i[j]==train_no:
                n=passenger_dict['ac']*i['ac_fare']+passenger_dict['sleeper']*i['sleeper_fare']
    return n
print(get_train_name(45200))
print(get_trains_for_day("Mo"))
print(get_total_fare(45200,{"sleeper":5, "ac":1}))
