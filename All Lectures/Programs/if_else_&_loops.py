# if-else

# 1️Even or Odd (if…else)
num = int(input("Enter a number for Even/Odd check: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

print("\n--------------------------------\n")

# 2️Positive, Negative or Zero (if…elif…else)
num = int(input("Enter a number to check Positive/Negative/Zero: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print("\n--------------------------------\n")

# 3️Leap Year Checker (if…elif…else)
year = int(input("Enter a year to check Leap Year: "))
if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

print("\n--------------------------------\n")

# 4️Maximum of Two Numbers (Ternary Operator)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
max_num = a if a > b else b
print("Maximum number is:", max_num)

print("\n--------------------------------\n")

# 5️Even or Odd (Ternary Operator)
num = int(input("Enter a number for Even/Odd check (ternary): "))
print("Even") if num % 2 == 0 else print("Odd")

print("\n--------------------------------\n")

# 6️Grade Calculator (if…elif…else)
marks = int(input("Enter marks out of 100: "))
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)

print("\n--------------------------------\n")

# 7️Absolute Value (Ternary Operator)
num = int(input("Enter a number to find absolute value: "))
abs_val = num if num >= 0 else -num
print("Absolute value:", abs_val)

# loops

# 1️Print ASCII characters from 65 to 90 (A-Z) using for loop
print("ASCII characters from A-Z:")
for i in range(65, 91):  # 65 to 90 are ASCII codes for A-Z
    print(chr(i), end=" ")
print("\n--------------------------------\n")

# 2️Print ASCII characters from a-z using for loop
print("ASCII characters from a-z:")
for i in range(97, 123):  # 97 to 122 are ASCII codes for a-z
    print(chr(i), end=" ")
print("\n--------------------------------\n")

# 3️Print ASCII characters from 0-9
print("ASCII characters from 0-9:")
for i in range(48, 58):  # 48 to 57 are ASCII codes for 0-9
    print(chr(i), end=" ")
print("\n--------------------------------\n")

# 4️Print ASCII table (first 128 characters) with their codes
print("ASCII table (0-127):")
for i in range(128):
    print(f"{i}: {chr(i)}", end="\t")
    if (i+1) % 8 == 0:  # 8 characters per line
        print()
print("\n--------------------------------\n")

# 5️Input a string and print its ASCII codes
text = input("Enter a string: ")
print("ASCII codes of the string:")
for ch in text:
    print(f"{ch} -> {ord(ch)}")
print("\n--------------------------------\n")

# 6️Input ASCII code range and print characters
start = int(input("Enter starting ASCII code: "))
end = int(input("Enter ending ASCII code: "))
print(f"Characters from ASCII {start} to {end}:")
for i in range(start, end+1):
    print(chr(i), end=" ")
print()
