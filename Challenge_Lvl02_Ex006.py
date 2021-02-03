"""
Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""
from math import sqrt

def Q(D):

    C = 50
    H = 30

    if D == 0 : 
        return 0
    return int( sqrt( ((2*C*D)/H) ) )

User_Input = input("Entre the nums separated by comma: ")

User_Input_List = User_Input.split(",")

User_Input_List_int = [int(i) for i in User_Input_List]

output_List = []

for i in range(0,len(User_Input_List_int)):
    output_List.insert (i , Q(User_Input_List_int[i]) )

output_List = [str(i) for i in output_List]

print(",".join(output_List))



