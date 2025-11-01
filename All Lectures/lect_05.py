# Chapter 2 Excercies
# Volume of Cylinder
import math
radius, length = eval(input("Enter the values of raduis and length with comma separated:"))
PI = math.pi
area = PI*math.pow(radius,2)
volume = area*length

print("The value of Cylinder is:", volume)

# Pound to Kilo conversion
pound = eval(input("Enter Pounds:"))
kg = pound*0.454
print("The conversion of Pound to Kilogram is:", kg, "kg")

# Energy of Water in Kg
int_temp,fnl_temp,M=eval(input("Enter the values of Initial temperature, Final temperature and weight of water in kg:"))
Q=(fnl_temp-int_temp)*4184*M
print("The energy is needed:",Q)

# Wind-Chill program

temperature = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "))
wind_speed = eval(input("Enter the wind speed in miles per hour (>= 2): "))
twc = 35.74 + 0.6215 * temperature \
      - 35.75 * math.pow(wind_speed, 0.16) \
      + 0.4275 * temperature * math.pow(wind_speed, 0.16)

print("The wind chill index is", round(twc, 5))

# Calculate the lenght covered by an object
v,a = eval(input("Enter the values of Velocity and Acceleration repectively:"))
length = (math.pow(v,2)/2*a)
print("The length is:",length,"meter")



# Initial Deposit Value
final_value = eval(input("Enter final account value: "))
annual_interest_rate_percent = eval(input("Enter annual interest rate in percent: "))
number_of_years = eval(input("Enter number of years: "))
monthly_interest_rate = annual_interest_rate_percent / 100 / 12
number_of_months = number_of_years * 12
initial_deposit = final_value / math.pow(1 + monthly_interest_rate, number_of_months)

print("Initial deposit value is", initial_deposit)
