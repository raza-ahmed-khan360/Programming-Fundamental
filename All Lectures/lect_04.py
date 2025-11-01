# Average of 5 numbers
num1,num2,num3,num4,num5=2,4,6,8,10

sum = num1+num2+num3+num4+num5
avg = sum/5

print("The sum of 5 numbers are:", sum)
print("The average of 5 numbers is:", avg)

num1 = float(input("Enter the value of num1:"))
print(num1, type(num1))
num2 = float(input("Enter the value of num2:"))
print(num2, type(num2))


sub1,sub2,sub3,sub4,sub5=eval(input("Enter subjects separated by commas repectively:"))

obt_marks=sub1+sub2+sub3+sub4+sub5
per=obt_marks/500*100
print("Obtained Marks:", obt_marks, "\n", "Percentage:", per)


# Arthematic Operators
no1,no2 = eval(input("Enter 2 numbers separated by commas:"))
print(no1, "==", no2, no1==no2)
print(no1, "!=", no2, no1!=no2)
print(no1, ">=", no2, no1>=no2)
print(no1, "<=", no2, no1<=no2)
print(no1, ">", no2, no1>no2)
print(no1, "<", no2, no1<no2)

# Logical Operators
x=15

print(x>5 and x>10)
print(not(x>5 and x>10))
print(x>5 and x<10)
print(x>5 or x<10)
