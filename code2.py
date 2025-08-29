print("WELCOME TO MY CALCULATOR!!!")

while True:
    print("\nChoose an operation:")
    print("1.addition")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.exit")
    
    operation=int(input("Enter your choice (1-5):"))
    
    if operation==5:
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
          print("Error: Division by 0 is not allowed as it may crash.")
        
        else:
          print("Quotient:", number1/number2)
    
  
    
    
    

