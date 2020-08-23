#PF-Prac-10
def string_both_ends(input_string):
    if len(input_string) < 2:
        return '-1'
    return input_string[0:2] + input_string[-2:]
	#start writing your code here

input_string="w"
print(string_both_ends(input_string))
