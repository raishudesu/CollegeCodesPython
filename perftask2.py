def main():
    print("Press 1 for computing the factorial of a number. \n"
          "Press 2 for computing the square of a number. ")
    user = int(input("Enter the module number: "))
    if user == 1:
        print(">>Module 1: Factorial<<")

        def factorial(x):
            user1 = 1
            while x >= 1:
                user1 = user1 * x
                x = x - 1
            return user1
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
        user3 = int(input("Enter the number: "))
        square = pow(user3, 2)
        print(square)
    else:
        print("Error")
    cond = input("Do you want to try again? Y or N: ")
    if cond == "Y":
        main()
    elif cond == "N":
        exit()


main()
