arr=[-15,8,-31,47,-2,19]

count=arr[0]
for i in range(len(arr)):
    if count>arr[i-1]:
        count=arr[i-1]
print(count)


count=arr[0]
for i in range(len(arr)):
    if count<arr[i-1]:
        count=arr[i-1]
print(count)