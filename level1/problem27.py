#PF-Prac-27
def check_for_ten(num1,num2):
    #start writing your code here
    if num1 == 10 or num2==10 or abs(num1-num2) == 10 or (num1+num2) == 10:
        return True
    else:
        return False
    
    
print(check_for_ten(10,9))
