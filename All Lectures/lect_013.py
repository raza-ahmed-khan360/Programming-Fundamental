for var in "string":
    if var == "i":
        break
    print(var)
print("the end")


for letter in "python":
    if letter == "y":
        break
    print(f"Current Letter: {letter}")

var = eval(input("Enter variable value (number):"))
while var>0:
    var-=1
    if var == 5:
        break
    print(f"Current Var value: {var}")
print("Program Complete")

for i in range(1,6):
    for j in range(1,6):
        if i==j:
            break
        print(f"i = {i}, j = {j}", end=" ")
    print()

####################################

for var in "string":
    if var == "i":
        continue
    print(var)
print("the end")


for letter in "python":
    if letter == "y":
        continue
    print(f"Current Letter: {letter}")


var = eval(input("Enter variable value (number):"))
while var>0:
    var-=1
    if var == 5:
        continue
    print(f"Current Var value: {var}")
print("Program Complete")


for i in range(1,6):
    for j in range(1,6):
        if i==j:
            continue
        print(f"i = {i}, j = {j}", end=" ")
    print()


c=0
for i in range(1,101):
    if (i%2 and i%5 and i%10):
        c+=1
        print(f"{i}", end=" ")
print(f"Total: {c}")

for value in range(0, 101):
    ch = chr(value)
    if 'A' <= ch <= 'Z' and '0' <= ch <= '9' :
        continue
    print(chr(value), end=" ")

add = 0
num = 0
while num<20:
    num+=1
    if num==10 or num==11:
        continue
    add+=num
    print(f"The sum is: {add}")

count = 1
while count <= 5:         
    print("\nBoy", count)
    marks = eval(input("Enter score: "))
    check = 1
    while check == 1:
        if marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F"
        check = 0
    print("Score:", marks, "Grade:", grade)
    count += 1


def add(i1,i2):
    result=0
    for i in range(i1, i2+1):
        result+=i
    return result
def main():
    print(f"Sum 1-10 is: {add(1,10)}")
    print(f"Sum 20-37 is: {add(20,37)}")
    print(f"Sum 35-44 is: {add(35,44)}")
main()
     
def table(no):
    for i in range(1,11):
        print(f"{no} x {i} = {no*i}")
table(eval(input("Enter Number:")))

