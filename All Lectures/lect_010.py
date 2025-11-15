# for i in range(150, 99, -5):
#     print(i, end=" ")

# Number Table
# no = eval(input("Enter number:"))
# for i in range(1,11):
#     print(f"{no} x {i} = {no*i}")

# Using with random
# import random
# no = random.randint(1,100)
# for i in range(1,11):
#     print(f"{no} x {i} = {no*i}")


# import random
# no = random.randint(1,100)
# for i in range(10,0,-1):
#     print(f"{no} x {i} = {no*i}")

# import random
# no = random.randint(1,100)
# for i in range(9,0,-2):
#     print(f"{no} x {i} = {no*i}")
    
# import random
# no = random.randint(1,100)
# for i in range(10,0,-2):
#     print(f"{no} x {i} = {no*i}")

# ce = 0
# for i in range(1,101):
#     if i%2==0:
#         ce=ce+1
#         print(f"{i}",end=" ")
# print(f"\n total even numbers are {ce}")

# co = 0
# for i in range(1,101):
#     if i%2!=0:
#         co=co+1
#         print(f"{i}",end=" ")
# print(f"\n total even numbers are {co}")

# nos = eval(input("Enter no of sub:"))
# total = nos*100
# add=0
# for i in range(1, nos+1):
#     print(f"marks of subjects {i}:", end=" ")
#     marks=eval(input())
#     add=add+marks
# print(f"marks obtained = {add}")
# score = add/total*100
# print(f"you got {add} marks, percentage = {score:.2f}%")
# grade=(
#     "A+" if score >= 90 and score <= 100 else
#     "A" if score >= 80 and score <= 89 else
#     "B" if score >= 70 and score <= 79 else
#     "C" if score >= 60 and score <= 69 else
#     "D" if score >= 50 and score <= 59 else
#     "Fail"
    
# )

# for i in range(65,91):
#     print(f"{i}--> {chr(i)}", end=" ")
#     print(f"{i+32}--> {chr(i+31)}", end=" ")

# import math
# for i in range(1,101):
#     print(f"{i} square= {math.pow(i,2)}", end=" ")
 
# import math
# for i in range(1,101,2):
#     add = math.pow(i,2)
#     print(f"{add} = {add + i}", end=" | ")

# for letter in "Python":
#     print("Current letter:", letter)

# text = "Hello World!!".upper()
# for i in text:
#     print(i, end=" | ")

# text = "Hello world".lower()
# for i in text:
#     if i in "aeiou":
#         print(i, end=" ")

# vc = 0
# text = "Hello world!!".lower()
# for i in text:
#     if i in "aeiou":
#         vc=vc+1
#         print(i, end=" ")
# print(f"Vowel count: {vc}")

# char = input("Enter a character: ")
# for i in char: 
#     print("Capital Letter" if 'A' <= i <= 'Z' else "Small Letter")

# While loop
# no = eval(input("Enter number:"))
# s= eval(input("Enter starting number:"))
# e= eval(input("Enter ending number:"))
# k= eval(input("Enter step size:"))
# i=5
# while i<=10:
#     print(f"{i} x {no} = {i*no}")
#     i=i+k   

# i = 1
# while i<=10:
#     print(i, end=" ")
#     i=i+1

# i = 1
# while i<=10:
#     print(i, end=" ")
#     i=i+2

# i = 0
# while i<=10:
#     print(i, end=" ")
#     i=i+2

# i = 10
# while i>=1:
#     print(i, end=" ")
#     i=i-1

# i = 10
# while i>=1:
#     print(i, end=" ")
#     i=i-2

# i = 11
# while i>=1:
#     print(i, end=" ")
#     i=i-2