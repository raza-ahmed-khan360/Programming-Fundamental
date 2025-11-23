# child_age = int(input("Enter the child's age in years: "))
# child_height = int(input("Enter the child's height in cm: "))
# if child_age >= 12:
#     print("Age is valid")
#     if child_height >= 140:
#         print("Height is valid")
#         print("Allowed on the roller coaster!")
#     elif 120 <= child_height <= 139:
#         print("Height is moderate")
#         guardian = input("Is a guardian present? (yes/no): ").lower()
#         if guardian == "yes":
#             print("Allowed on the roller coaster with guardian")
#         else:
#             print("Not allowed without guardian")
#     else: 
#         print("Height is too low")
#         print("Not allowed on the roller coaster")
# else:
#     print("Age is too low")
#     print("Not allowed on the roller coaster")

# enrollment = input("Enter enrollment status (full-time/part-time): ").lower()
# gpa = eval(input("Enter GPA: "))
# if enrollment == "full-time":
#     if gpa >= 3.5:
#         room = "Single Room"
#     elif 3.0 <= gpa < 3.5:
#         room = "Shared Room"
#     else:
#         room = "No Room Assigned"
# else:
#     room = "No Room Assigned (Part-time students not eligible)"
# print(f"Hostel Assignment: {room}")

# purchase = eval(input("Enter purchase amount: "))
# loyalty_member = input("Are you a loyalty member? (yes/no): ").lower()
# if purchase >= 500:
#     if loyalty_member == "yes":
#         discount = 20  
#     else:
#         discount = 15  
# elif 200 <= purchase < 500:
#     if loyalty_member == "yes":
#         discount = 10  
#     else:
#         discount = 5   
# else:
#     discount = 0      
# print(f"Discount applicable: {discount}%")

# print("=== Candidate Shortlisting ===")
# degree = input("Do you have a Bachelor's degree? (yes/no): ").lower()
# experience = eval(input("Enter years of experience: "))
# skills_score = eval(input("Enter skills test score (0-100): "))
# if degree == "yes":
#     if experience >= 3:
#         result = "Shortlisted"
#     else:
#         if skills_score >= 80:
#             result = "Shortlisted"
#         else:
#             result = "Rejected"
# else:
#     result = "Rejected"
# print(f"Candidate Status: {result}")


# n = eval(input("Enter number of items: "))
# print("Enter item name and days remaining separated by space:")
# for i in range(n):
#     item, days = input(f"Item {i+1}: ").split()
#     days = eval(days)
#     if days < 3:
#         print(f"{item} - {days} day(s) remaining")


# print("School Attendance Marking System")
# print("Marking attendance for the following roll numbers:")
# for i in range(1, 11):
#     print(f"Roll Number: {i}")


# print("Enter calories burned for each minute:")
# total_calories = 0
# for i in range(1, 6):
#     calories = eval(input(f"Minute {i}: "))
#     total_calories += calories
# print(f"Total calories burned in 5 minutes: {total_calories}")


# correct_pin = input("Set your ATM PIN: ")
# attempts = 3
# while attempts > 0:
#     pin = input("Enter your ATM PIN: ")
#     if pin == correct_pin:
#         print("Access Granted")
#         break 
#     else:
#         attempts -= 1
#         if attempts > 0:
#             print(f"Incorrect PIN. You have {attempts} attempt(s) left.")
#         else:
#             print("All attempts failed. Your card is blocked.")

# print("Restaurant Token Counter")
# token = 1
# while token <= 50:
#     print(f"{token}", end=" ")
#     token += 1 

# total_cars = 8 
# exited_cars = 0
# print("Parking Garage Exit System")
# while exited_cars < total_cars:
#     exited_cars += 1
#     print(f"Car {exited_cars} has exited")
# print("All cars have exited the garage")

# rows = 4
# columns = 6
# roll_number = 101  
# print("Exam Seating Chart:")
# for r in range(1, rows + 1):
#     for c in range(1, columns + 1):
#         print(f"{roll_number}", end="\t") 
#         roll_number += 1
#     print()



# print("All possible menu combinations:")
# for i in range(1, 4):  # Starters 1 to 3
#     for j in range(1, 5):  # Drinks 1 to 4
#         # Map numbers to names
#         if i == 1:
#             starter = "Soup"
#         elif i == 2:
#             starter = "Salad"
#         else:
#             starter = "Fries"
#         
#         if j == 1:
#             drink = "Juice"
#         elif j == 2:
#             drink = "Cola"
#         elif j == 3:
#             drink = "Water"
#         else:
#             drink = "Lemonade"
#         
#         print(f"{starter} + {drink}")


# total_users = 5  
# print("=== Login Simulator ===")
# 
# for user in range(1, total_users + 1):
#     print(f"\nTesting Username {user}")
#     attempts = 3          
#     logged_in = False     
#     
#     while attempts > 0 and not logged_in:
#         pwd = input("Enter password: ")
# 
#         if pwd == "pass123":      
#             print("Login Successful!")
#             logged_in = True
#         else:
#             attempts -= 1
#             if attempts > 0:
#                 print(f"Incorrect password. {attempts} attempt(s) left.")
#             else:
#                 print("This username is locked.")
# 
# print("\nAll usernames tested. Simulation complete.")


# total_units = 10
# sensors = 3  
# print("=== Production Line Quality Check ===")
# for unit in range(1, total_units + 1):
#     print(f"\nChecking Unit {unit}:")
#     for sensor in range(1, sensors + 1):
#         if sensor == 1:
#             print("  Sensor#1: Weight check")
#         elif sensor == 2:
#             print("  Sensor#2: Dimensions check")
#         else:
#             print("  Sensor#3: Temperature check")

        







