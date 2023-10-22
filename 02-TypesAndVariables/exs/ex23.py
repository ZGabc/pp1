import math

a = int(input("enter a: "))
b = int(input("enter b: "))
c = float(input("enter c: "))

p = (a + b + c)/2
S = math.sqrt(p*(p-1)*(p-b)*(p-b))

print(S)