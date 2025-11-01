num1,num2,num3=map(eval, input("Enter values of 3 number:").split())
sum=num1+num2+num3
avg=sum/3
print(f"The Sum of {num1}, {num2} and {num3} is {sum} \nThe Average of {num1}, {num2} and {num3} is {round(avg, 2)}")

# use of max() and min()
res1 = eval("max(12,5,-5)")
print(res1)
res2 = eval("min(-122,5,5)")
print(res2)

# len() example
print(eval("len('Hello World')"))

# global and local
x,y=12,34
z=eval("x+y", {"x":10},{"y":17})
print(x,y,z)

# .upper() .lower() .title
name = "I am Raza Ahmed"
print(name.upper(),"\n",name.lower(),"\n",name.title())

# Another program with map() and .split() and input()
x,y=map(int, input("Enter two numbers:").split())
print(f"x = {x}, y = {y} sum is: {x+y}")

# using :.f
val=3.14159265358979323
print(f"The value of 3 decimal {val:.3f}")
print(f"The value of 1 decimal {val:.1f}")
