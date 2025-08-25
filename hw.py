num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Modulus")

choice = int(input("Enter your choice(1-4):"))
if choice == 1:
    print("Result =", num1 + num2)
elif choice == 2:
    print("Result =", num1 - num2)
elif choice == 3:
    print("Result =", num1 * num2)
elif choice == 4:
    if num2 != 0:   
        print("Result =", num1 % num2)
    else:
        print("Error: Cannot take modulus by 0")
else:
    print("Invalid choice! Please select between 1-4.")
    print = input("Do you want to perform another operation? (yes/no): ")
    print("Okay Let's continue...")
