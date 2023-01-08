from cmath import sqrt
import math
a=int(input("a is equal: "))
b=int(input("b is equal: "))
c=int(input("c is equal: "))
p=(a+b+c)*1/2
wzor=p*(p-a)*(p-b)*(p-c)

if wzor <= 0:
    print("to nie jest trójkąt")
else:
    print(math.sqrt(wzor))

