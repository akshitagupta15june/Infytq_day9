#PF-Prac-9
def generate_dict(number):
    d=dict()
    for x in range(1,number+1):
        d[x]=x**2
    
    return d 
	#start writing your code here

number=20
print(generate_dict(number//2))
