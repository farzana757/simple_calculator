print("WELCOME TO MY CALCULATOR!!!")

while True:
    print("\nChoose an operation:")
    print("1.Addition")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Modulus")
    print("6.Power")
    print("7.Exit")
    
    operation=int(input("Enter your choice (1-7):"))
    
    if operation==7:
      print("Exiting calculator, Goodbye")
      break
    
    number1= int(input("Enter the first number:"))
    number2= int(input("Enter the second number:"))
   
    if operation==1:
      print("Sum:", number1 + number2)
    
    elif operation==2:
        print("Difference:", number1-number2)
    
    elif operation==3:
        print("Product:", number1*number2)
    
    elif operation==4:
        if number2==0:
          print("Error: Division by 0 is not allowed.")
        
        else:
          print("Quotient:", number1/number2)
    
    elif operation==5:
        if number2==0:
          print("Error: Modulus by 0 is not allowed.")
            
        else:
          print("Modulus:", number1%number2)
          
    elif operation==6:
        print("Power:", number1**number2)
    
    else:
        print("Error: Please enter the number between (1-7)")
    
    

