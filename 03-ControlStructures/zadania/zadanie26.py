for i in range(4):
    if i==3:
        print("Sorry, your payment card has been blocked")
    else:
         PIN=input("Enter the PIN code: ")
         if PIN=="0805":
             print("correct PIN")
             break 
         else:
             print("Incorrect PIN")


