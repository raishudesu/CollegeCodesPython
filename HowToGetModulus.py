#STEP 1: identify the first integer by user input
#STEP 2: indentify the second integer by user input
#STEP 3: create an if statement
#STEP 4: identify the formula of modulus which should equal to 0 (x % y == 0)
#STEP 5: define the result

x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))

if x % y == 0:
    print("The first number is divisible by the second number!")
else:
    print("The first number is not divisible by the second number!")
