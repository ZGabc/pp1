def integers(n):
    for i in range(1,n+1):
        print(i, end=" ")

def main():
    z=int(input("how many integers? "))
    integers(z)

main()