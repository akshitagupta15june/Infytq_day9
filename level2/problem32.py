#PF-Prac-32
def check_squares(number):
    #start writing your code here
    
    i = 1 
    while i * i <= number : 
        j = 1
        while(j * j <= number) : 
            if (i * i + j * j == number) : 
                 
                return True
            j = j + 1
        i = i + 1
          
    return False


number=68
print(check_squares(number))
