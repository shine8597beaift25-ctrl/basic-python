m = int(input("Enter your marks"))
if m>100:
    print("Error")
    m = int(input("Enter your marks"))
    if m<0:
        print("ERROR again")
        m = int(input("Enter your marks"))
    if m>=90:
        print("Grade : A+")
    elif m>=75:
        print("Grade : A")
    elif m>=60:
        print("Grade : B")
    elif m>=40:
        print("Grade : C")
    else:
        print("Fail")