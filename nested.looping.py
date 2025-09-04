# print("Day5")
# print("Todays Topic is Nested looping")

# for i in range(1,4):
#     for j in range(1,4):
#         print(i*j,end=" ")
#     print()

# n =11
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
     
# n = 7
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end = " ")
#     print()

# rows = 8
# num = 1
# for i in range(1,rows+1):
#     for j in range(i):
#         print(num,end = " ")
#         num+=1
#     print()


# num = 8
# for i in range(1,num+1):
#     for j in range(num-i):
#         print("*",end=" ")
#     print()


# num = 6
# for i in range(6):
#     for j in range(num+i):
#         print(" ","*",end=" ")
#     print()

#ulta right angle triangle
print("Ulta Right angle triangle:-")
n = int(input("enter a number:"))
for i in range(1, n+1):
    for j in range(n - i): 
        print(" ", end=" ")
    for k in range(i):       
        print("*", end=" ")
    print()



#circle making
#
