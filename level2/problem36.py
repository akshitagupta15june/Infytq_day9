def find_target_positions(input_string, target_word):
    target_list=[]
    #Start writing your code here
    input_string=input_string.split(" ")
    count=0
    for i in input_string:
    	if i==target_word:
    		target_list.append(count)
    	count+=1


    return target_list

def find_inverted_index(input_string):
    target_dict={}
    #Start writing your code here
    input_string=input_string.split(" ")
    for i in input_string:
    	target_dict[i]=find_target_positions(" ".join(input_string),i)

    
    return target_dict
    
    
input_string="we dont need no education we dont need no thought control no we dont"
print(find_target_positions(input_string,'dont'))
result_dict=find_inverted_index(input_string)
print(result_dict)
