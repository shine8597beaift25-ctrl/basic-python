#Write a program to check whether a given number is greater than 100 and divisible by 5 (use relational and logical operators)
num=int(input("Enter a number:"))
if num > 100 and num % 5 == 0:
    print(num,"is greater than 100 and divisible by 5.")
else:
    print(num," does not satisfy the condition.")