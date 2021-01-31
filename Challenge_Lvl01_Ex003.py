from math import pow

Pow2_Obj = {}

n = int(input("give us the integral num: "))

for i in range (1,n+1):

    Pow2_Obj[i] = int(pow(i,2))

print("the result: ",Pow2_Obj)
