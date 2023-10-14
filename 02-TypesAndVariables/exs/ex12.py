i = int(input("how many people are making money in your family: "))
people = int(input("how many people are there in you family: ")) 
sum = 0
z = 0
while z < i:
    n = int(input("Enter income: "))
    sum+=n
    z+=1
    
print(f"income per person: {sum/people}")
