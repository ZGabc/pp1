arr=[[3,9,2],[2,4,5],[7,1,6],[0,4,8]]

i=0
j=0
even=0
while i<=len(arr):
    while j<=len(arr[i]):
        if arr[i-1][j-1]%2==0:
            even=even+arr[i-1][j-1]
            j+=1
        i+=1


    
    
    
