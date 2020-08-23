#PF-Prac-11
def find_upper_and_lower(sentence):
    #start writing your code here
    sentence=list(sentence)
    d=[]
    dup=0
    dlo=0
    for c in sentence:
        if c.isupper():
           dup+=1
        elif c.islower():
           dlo+=1
        else:
           pass
    d.append(dup)
    d.append(dlo)
       
    return d

sentence="Come Here"
print(find_upper_and_lower(sentence))
