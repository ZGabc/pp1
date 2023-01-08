from html.entities import codepoint2name


amount=int(input("enter the amount in PLN "))

coin5= amount//5
coin2=(amount-coin5*5)//2
coin1=amount-coin5*5-coin2*2

print("5 zł:",coin5)
print("2 zł:",coin2)
print("1 zł:",coin1)