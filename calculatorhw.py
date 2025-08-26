while True:
    s = int(input("Enter first number: "))
    n = int(input("Enter second number: "))
    
    print("Choose operation:")
    print("1. + Addition")
    print("2. - Subtraction")
    print("3. * Multiplication")
    print("4. / Divison")
    print("5. % Modulus")

    operation = input("Enter operation: ")

    if operation == "+":
        print("Result:", s + n)
    elif operation == "-":
        print("Result:",  s-n)
    elif operation == "*":
        print("Result:", s * n)
    elif operation == "/":
        print("Result:", s / n)
    elif operation == "%":
        print("Result:", s%n)
    else:
        print("Invalid operation")

    again=input("Wanna Continue? (yes/no):")
    if again == "no":
        print("The End")
        break
    elif again == "yes":
         print("Let's do it again")
    else:
        print("Invalid")