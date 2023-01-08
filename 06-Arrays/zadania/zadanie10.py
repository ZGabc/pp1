arr=[23,43,45,53,4]
i=0
even=0
odd=0
while i<len(arr):
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1
    i+=1
print("even: ",even, "odd:", odd)
       
