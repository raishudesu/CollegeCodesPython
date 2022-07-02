num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "addition":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "subtraction":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "division":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
elif op == "multiplication":
    print(num1 * num2)
else:
    print("Invalid operator!")
