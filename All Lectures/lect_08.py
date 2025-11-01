import math
radius = eval(input("Enter radius:"))
if (radius>=0):
    area = math.pi*math.pow(radius,2)
    print(f"radius={radius}, area={area:.2f}")
else:
    print(f"{radius} is negative")

no = eval(input("Enter an integer:"))
if (not(no%2)):
    print(f"{no} is even")
else:
    print(f"{no} is odd")
    
# leap year program
year = eval(input("Enter year:"))
if (year%4==0):
    print(f"The {year} is leap")
else:
    print(f"The {year} is not leap")
    
    
# Fully Working Marksheet
sub1,sub2,sub3,sub4,sub5=map(eval,input("Enter the numbers of subjects:").split())
marks=sub1+sub2+sub3+sub4+sub5
per=marks/500*100

if (per>=50) and (per<=59):
    print("Your grade is D")
elif (per>=60) and (per<=69):
    print("Your grade is C")
elif (per>=70) and (per<=79):
    print("Your grade is B")
elif (per>=80) and (per<=89):
    print("Your grade is A")
elif (per>=90) and (per<=100):
    print("Your grade is A+")    
else:
    print("You are fail")

