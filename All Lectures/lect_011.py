no = 0
add = 0
while no!=-1:
    add = add+no
    no=eval(input("Enter no greater than 0 to continue: "))
print(f"Sum = {add}")

run = 'y'

while run.lower() == 'y':
    o1 = eval(input("Enter operand 1: "))
    o2 = eval(input("Enter operand 2: "))
    op = int(input("Enter operation (1 for sum, 2 for difference): "))
    
    if op == 1:
        print(f"The sum of {o1} and {o2} is {o1 + o2}")
    elif op == 2:
        print(f"The difference of {o1} and {o2} is {o1 - o2}")
    else:
        print("Invalid operation!")
    run = input("Do you want to continue? (y/n): ")

age = 20
if age > 10:
    if age < 30:
        print("Age is between 10 and 30")

ch='A'
if ch in 'AEIOUaeiou':
    if ch.isupper():
        print("Uppercase Vowel")
    else:
        print("Lowercase Vowel")

username='admin'
password='1234'
if username=='admin':
    if password=='1234':
        print("Login successful")
    else:
        print("Incorrect Password!")
else:
    print("Invalid Role!!!")

balance=5000
withdraw=2000
pin=1234
entered_pin=12234
if entered_pin==pin:
    if withdraw<=balance:
        print("Transition Successful")
    else:
        print("Insufficient Balance")
else:
    print("Invalid Pin!")




        
