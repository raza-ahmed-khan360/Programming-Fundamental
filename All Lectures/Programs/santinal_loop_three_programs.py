run = 'y'

while run.lower() == 'y':
    print("\n=== Program Menu ===")
    print("1. Calculator")
    print("2. Marksheet")
    print("3. Area of Circle")
    print("4. Exit")
    
    choice = input("Enter the number of the program to run: ")

    # ---------------- CALCULATOR ----------------
    if choice == '1':
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

        no1, no2 = map(int, input("Enter 2 numbers separated by space: ").split())
        choice_calc = input("Enter the Choice: ")

        if choice_calc == '1' or choice_calc == 'a' or choice_calc == 'A' or choice_calc == '+':
            print("Sum =", no1 + no2)

        elif choice_calc == '2' or choice_calc == 's' or choice_calc == 'S' or choice_calc == '-':
            print("Difference =", no1 - no2)

        elif choice_calc == '3' or choice_calc == 'm' or choice_calc == 'M' or choice_calc == '*':
            print("Product =", no1 * no2)

        elif choice_calc == '4' or choice_calc == 'd' or choice_calc == 'D' or choice_calc == '/':
            print("Division =", no1 / no2)

        elif choice_calc == '5' or choice_calc == 'r' or choice_calc == 'R' or choice_calc == '%':
            print("Remainder =", no1 % no2)

        elif choice_calc == '6' or choice_calc == 'f' or choice_calc == 'F' or choice_calc == '//':
            print("Floor Division =", no1 // no2)

        elif choice_calc == '7' or choice_calc == 'e' or choice_calc == 'E' or choice_calc == '**':
            print("Exponential =", no1 ** no2)

        else:
            print("Invalid Choice!!")

    # ---------------- MARKSHEET ----------------
    elif choice == '2':
        nos = eval(input("Enter no of subjects: "))
        total = nos * 100
        add = 0

        i = 1
        while i <= nos:
            print(f"Marks of subject {i}: ", end="")
            marks = eval(input())
            add = add + marks
            i += 1

        print(f"Marks obtained = {add}")
        score = add / total * 100
        print(f"Percentage = {score:.2f}%")

        if 90 <= score <= 100:
            print("Grade: A+")
        elif 80 <= score <= 89:
            print("Grade: A")
        elif 70 <= score <= 79:
            print("Grade: B")
        elif 60 <= score <= 69:
            print("Grade: C")
        elif 50 <= score <= 59:
            print("Grade: D")
        else:
            print("Grade: Fail")

    # ---------------- AREA OF CIRCLE ----------------
    elif choice == '3':
        import math
        radius = float(input("Enter radius: "))
        area = math.pi * (radius ** 2)
        print("Area of circle =", area)

    # ---------------- EXIT ----------------
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice!")

    run = input("Do you want to run another program? (y/n): ")