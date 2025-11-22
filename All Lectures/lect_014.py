import random
def table(no):
    for i in range(1,10+1):
        print(f"{no} x {i} = {no*1}")
def main():
    table(random.randint(1,100))
main()

import math
def add(no1, no2):
    return no1+no2
def sub(no1, no2):
    return no1-no2
def mul(no1, no2):
    return no1*no2
def div(no1, no2):
    return no1/no2
def area(rad):
    return math.pi*math.pow(rad,2)

def main():
    print(f"sum={add(123,456)}, sub={sub(9,3)}, mul={mul(4,6)}, div={div(5,2)}, area={area(2)}")
main()

def nprintln(message,n):
    for i in range(1,n+1):
        print(message, end=" ")
nprintln(n=10, message="Hello!")
nprintln("Hello!",10)
nprintln(10,"Hello!") # Will throw type error

x = 1
def increase():
    global x
    x += 1
    print(x)
increase()
print(x)
