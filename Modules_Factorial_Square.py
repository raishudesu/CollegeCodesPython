def factorial(x):
    user1 = 1
    while x >= 1:
        user1 = user1 * x
        x = x - 1
    return user1
def square(x):
    square = pow(x, 2)
    print(square)
def main():
    print("Press 1 for computing the factorial of a number. \n"
          "Press 2 for computing the square of a number. ")
    user = int(input("Enter the module number: "))
    if user == 1:
        print(">>Module 1: Factorial<<")
        user2 = int(input("Enter the number: "))
        f = factorial(user2)
        print("Factorial: ", f)
        cond = input("Do you want to try again? Y or N: ")
        if cond == "Y":
            main()
        elif cond == "N":
            exit()
    elif user == 2:
        print(">>Module 2: Square of a number")
        x = int(input("Enter the number: "))
        square(x)
    else:
        print("Error")
    cond = input("Do you want to try again? Y or N: ")
    if cond == "Y":
        main()
    elif cond == "N":
        exit()
main()
