print("""
*****Welcome to BSIT Bank!*****
[1] Deposit
[2] Withdraw
[3] Transaction History
[4] Exit
""")

def deposit():
    dep = 0
    while dep <= 0:
        print(" ")
        dep = float(input("Enter amount to deposit: "))
        if dep > 1:
            return dep
   
def bankop():
    dep = 0
    totalbalance = 0
    main_record = []
    while 1:
        print('')
        user = int(input("Enter your choice!: "))
        if user == 1:
            dep = deposit()
            totalbalance += dep
            print("You deposited: ", dep)
            print("Your balance is now: ", totalbalance)
            main_record.append(["Deposit: ", dep])
        
        elif user == 2:
            while 1:
                withdraw = float(input("Enter amount to withdraw: "))
                if withdraw > totalbalance:
                    print("Withdraw in less than your current balance!")
                elif withdraw <= totalbalance:
                    totalbalance = (totalbalance - withdraw)
                    print("You withdrew: ", withdraw)
                    print("Your balance is now: ", totalbalance)
                    main_record.append(["Withdrawal: ", withdraw])
                    break
       
        elif user == 3:
            for i in main_record:
                print(*i, sep = "")
            print("\n") 
            print("Total balance: ", totalbalance)
        elif user == 4:
            exit()
        else:
            print("Invalid Value!")

bankop()