def calculator():
    while True:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Cannot divide by zero.")
                continue
        else:
            print("Invalid operator.")
            continue

        print(f"{num1} {operator} {num2} = {result}")

        again = input("Do you want to calculate again? (y/n): ")

        if again.lower() != "y":
            print("Goodbye!")
            break


calculator()