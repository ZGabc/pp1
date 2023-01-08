arr=[15, 8, 31, 47, 2, 19]

count=0
i=0
while i <len(arr):
    count+=arr[i]
    i+=1

print(count/len(arr))