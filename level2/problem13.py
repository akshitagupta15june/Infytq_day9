def close_number(num1,num2,num3):
    list=[]
    cou=0
    list.append(num1-num2)
    list.append(num1-num3)
    list.append(num2-num1)
    list.append(num2-num3)
    list.append(num3-num1)
    list.append(num3-num2)
    for i in list:
        if abs(i)==1 or i==0:
            cou=cou+1
    if(cou==2):
        return True
    return False
    #start writing your code here
    
print(close_number(5,4,2))
