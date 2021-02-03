"""
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
"""

User_Input = input("entre your nums separeted by comma: ")
User_Input_List = User_Input.split(",")
User_Input_List_int = [int (i) for i in User_Input_List ] 

rows = User_Input_List_int[0] 
column = User_Input_List_int[1]

multiList = [[0 for col in range(column)] for row in range(rows)]

for i in range (rows):
    for j in range (column):
        multiList[i][j] = i*j


print(multiList)


