#PF-Prac-38
def build_index_grid(rows, columns):
    result_list = [[0 for col in range(columns)] for row in range(rows)]

    for row in range(rows):
        for col in range(columns):
            result_list[row][col]= row*col
        
        
    

    return result_list

rows=4
columns=3
result=build_index_grid(rows,columns)
print("Rows:",rows,"Columns:",columns)
print("The matrix is:",result)
for i in result:
    print(i)
