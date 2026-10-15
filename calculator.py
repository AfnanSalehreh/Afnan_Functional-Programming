def calculator():
    while True:
        try:
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
                result = num1 / num2
            else:
                print("Invalid operator.")
                continue

            print(f"{num1} {operator} {num2} = {result}")

        except ValueError:
            print("Please enter valid numbers.")

        except ZeroDivisionError:
            print("Cannot divide by zero.")

        again = input("Do you want to calculate again? (y/n): ")

        if again.lower() != "y":
            print("Goodbye!")
            break


calculator()

