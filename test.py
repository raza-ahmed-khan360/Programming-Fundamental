import math

radius, length = eval(input("Enter the values of radius and length respectively:"))
PI = 3.1416

area = PI*math.pow(radius,2)
volume = area*length

print("The area of given values are:", area)
print("The volume of given values are:", volume)