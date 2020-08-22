def longest_common_substring(string1, string2):
    maxs=""
    final=[]
    for i in range(len(string1)):
        if string1[i] in string2:
            maxs=string1[i]
        for j in range(i+1,len(string1)):
            if maxs+string1[j] in string2:
                temp=maxs+string1[j]
                if len(maxs)>len(temp):
                    continue
                else:
                    maxs=temp
                    if j==len(string1)-1:
                        return maxs
            else:
                break
    return maxs  
    
    return string1[x_longest - longest: x_longest]
    
   

output=longest_common_substring("discatenation","concatenation")
print("The longest overlap of characters between string1 and string2:",output)
output1=longest_common_substring("assured","measured")
print("The longest overlap of characters between string1 and string2:",output1)
