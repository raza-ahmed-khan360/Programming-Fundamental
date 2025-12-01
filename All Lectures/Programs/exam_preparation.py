# Loops practice

# for i in range (1,11):
#     print(i)

# i=1
# while i<=10:
#     print(i)
#     i+=1

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,"x",j,"=",i*j)
#

# for i in range(1,5):
#     for j in range(1,5):
#         print("*",end=" ")
#     print()

# while True:
#     msg=input("Enter message here (or write 'exit/q/quit' to stop):").lower()
#     if msg == "exit" or msg == "q" or msg =="quit":
#         break
#     print("You have wrote", msg)

# Patterns
# for i in range(1,5):
#     for j in range (1,5):
#         print("*",end=" ")
#     print()

# i=0
# while i<5:
#     j=0
#     while j<5:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# i=1
# while i<=7:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j,end=' ')
#         j+=1
#     i+=1
#     print()
    
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# i=5
# while i>0:
#     j=0
#     while j<i:
#         print("*",end=" ")
#         j+=1
#     i-=1
#     print()

# rows=5
# for i in range(rows):
#     print(" " * (rows-i-1),end=" ")
#     print("*" * (2*i+1))


# for i in range(1, 5):
#     for j in range(1, 5):
#         if j % 2 == 0:
#             print("*", end=" ")
#         else:
#             print(j, end=" ")
#     print()
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         if j % 2 == 0:
#             print("*", end=" ")
#         else:
#             print(j, end=" ")
#     print()

# for i in range(1, 5):
#     for j in range(1, 5):
#         if i == j:
#             print("*", end="")
#         else:
#             print("O", end="")
#     print()

# num = int(input("Enter number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# n = int(input("Enter number: "))
# for i in range(1,n+1):
#     print(i)
    
# n = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")

# num1,num2,num3=eval(input("Enter three numbers separated by comma: "))
# print(max(num1,num2,num3))

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# import math
# num = int(input("Enter a number: "))
# for i in range(1,num+1):
#     print(math.factorial(i))

# n = int(input("Enter a Number: "))
# for i in range(1,n):
#     if n%2==0:
#         n+=1
#     print(n)

# P=int(input("Enter number: "))
# R=int(input("Enter number: "))
# T=int(input("Enter number: "))
# SI = (P * R * T) / 100
# print(SI)

# word = input("Enter a word: ")
# print(len(word))

# num = int(input("Enter a number: "))
# for i in range(num,0,-1):
#     print(i)

# n = int(input("Enter a number: "))
# for i in range(1, n+1, 2):   # start=1, stop=n+1, step=2
#     print(i)


# n = int(input("Enter a number: "))
# sum_odd=0
# for i in range(1, n+1, 2):   # start=1, stop=n+1, step=2
#     sum_odd+=1
# print(sum_odd)

# n = int(input("Enter a number: "))
# sum_odd=0
# for i in range(1, n+1):
#     if i%2!=0:
#         print(i)
#         sum_odd+=i
# print(sum_odd)

    
    