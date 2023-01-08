for i in range(30):
    if (i+1)%3==0 and (i+1)%5==0:
        print("BINGO")
    elif(i+1)%3==0:
        print("THREE")
    elif (i+1)%5==0:
        print("FIVE")
    else:
        print(i+1)
        