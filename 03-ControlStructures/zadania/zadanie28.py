for i in range(51):
    if i<2:
        print(i)
        z=1
    elif i==2:
        print(1)
        j=1
    else:
        k=z+j
        print(k)
        z=j
        j=k
