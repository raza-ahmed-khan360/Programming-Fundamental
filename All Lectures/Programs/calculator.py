# calculator
print(
"""
1. Write '1' or 'a' or 'A' or '+' for Addition
2. Write '2' or 's' or 'S' or '-' for Subtraction
3. Write '3' or 'm' or 'M' or '*' for Multiplication
4. Write '4' or 'd' or 'D' or '/' for Division
5. Write '5' or 'r' or 'R' or '%' for Modulus
6. Write '6' or 'f' or 'F' or '//' for Floor Division
7. Write '7' or 'e' or 'E' or '**' for Exponential
"""
)

no1,no2=map(eval,input("Enter 2 number separated by space:").split())
choice=eval(input("Enter the Choice:"))

if (choice=='1' or choice=='a' or choice=='A' or choice=='+'):
    ans=no1+no2
    print(f"The Sum of {no1} and {no2} is = {ans}")
elif (choice=='2' or choice=='s' or choice=='S' or choice=='-'):
    ans=no1-no2
    print(f"The Difference of {no1} and {no2} is = {ans}")
elif (choice=='3' or choice=='m' or choice=='M' or choice=='*'):
    ans=no1*no2
    print(f"The Multiple of {no1} and {no2} is = {ans}")
elif (choice=='4' or choice=='d' or choice=='D' or choice=='/'):
    ans=no1/no2
    print(f"The Division of {no1} and {no2} is = {ans}")
elif (choice=='5' or choice=='r' or choice=='R' or choice=='%'):
    ans=no1%no2
    print(f"The Reminder of {no1} and {no2} is = {ans}")
elif (choice=='6' or choice=='f' or choice=='F' or choice=='//'):
    ans=no1//no2
    print(f"The Floor Division of {no1} and {no2} is = {ans}")
elif (choice=='7' or choice=='e' or choice=='E' or choice=='**'):
    ans=no1**no2
    print(f"The Difference of {no1} and {no2} is = {ans}")
else:
    print("Invalid Choice!!")
