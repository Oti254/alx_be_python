num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"The result is {int(num1) +int(num2)}.")
match operation:
    case "-":
        print(f"The result is {int(num1) - int(num2)}.")
match operation:
    case "*":
        print(f"The result is {int(num1) * int(num2)}.")
match operation:
    case "/":
        if num2 == 0:
            print(f"Cannot divide by zero.")
        else:
            print(f"The result is {int(num1) / int(num2)}.")

