def seed_no(number,ref_no):
    #start writing your code here
    n=str(number)
    tot=1
    for i in n:
        tot=tot*int(i)
    if(tot*number==ref_no):
        return True
    return False
    
number=123
ref_no=738
print(seed_no(number,ref_no))
