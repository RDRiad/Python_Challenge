"""
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

"""

def fact(n):
    if n == 0 :
        return 1
    return fact(n-1) * (n)

n = int(input("Please entre your factoriele number : "))

print(f"the result is : {fact(n)}")
