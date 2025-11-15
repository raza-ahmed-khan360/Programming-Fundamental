# For loops
x = 2
if x > 0:
    y = 1
    print(f"If Block Executed {y}")
else:
    y = -1
    print(f"Else Block Executed {y}")

# Ternary operator
x = 2
y = 1 if x > 0 else -1
print(y)

z = eval(input("Enter char:")).lower()
char = "Vowel" if z == 'a' or z == 'e' or z == 'i' or z == 'o' or z == 'u' else "Consonant"
print(char)

year = int(input("Enter a year: "))

# Leap Year
leap = "Leap Year" if (year % 400 == 0) else "Leap Year" if (year % 4 == 0 and year % 100 != 0) else "Not Leap Year"
print(leap)

for i in range(100,151,4):
    print(i,end=" ")

