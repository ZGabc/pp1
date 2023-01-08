import random

roll=random.randint(1,6)
user=int(input("guess the number: "))

if user==roll:
    print(True)
else:
    print(False)


