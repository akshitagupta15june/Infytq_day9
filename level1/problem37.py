#PF-Prac-37
def sum_of_list(num_list): 
    total = 0
    for x in num_list:
        total += x
    return total

	

num_list=[44,23,77,11,89,3]
result=sum_of_list(num_list)
print("Sum of the elements:",result)
