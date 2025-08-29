print ("WELCOME TO MY CALCULATOR")
number1 = int(input("Enter your first number:"))
number2 = int(input("Enter your second number:"))



add = number1 + number2
subtract = number1 - number2
multiply= number1 * number2
divide= number1/ number2

operation= int(input("Enter the operation:"))
'''add==1
subtract==2
multiply==3
divide==4'''


if operation==1:
    print("Sum of number1 and number2 is:",add)
 
elif operation== 2:
    print("Difference of number1 and number2:", subtract)
    
elif operation== 3:
    print("Product of number1 and number2:", multiply)

elif operation== 4:
    print("Quotient of number 1 and number2:", divide)
    
else:
    print("Exit")
    

