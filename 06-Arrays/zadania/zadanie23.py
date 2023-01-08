def bubblesort(arr):
    i=0
    count=arr[i]
    print(arr)
    for i in range(len(arr)):
        if count<arr[i]:
            count=arr[i]
            arr[i]=count
        else:
            d=6
    return(arr)

print(bubblesort([23,4,23]))