'''
Corrie Stewart
Program simulates an ATM machine
Date: 10/14/18
'''

class Account:
    def __init__(self, id = 0, balance = 100):
        self.__id = id
        self.__balance = balance

    def getId(self):
        return self.__id

    def getBalance(self):
        return format(self.__balance, ".2f")

    def setID(self, id):
        self.__id = id

    def setBalance(self, balance):
        self.__balance = balance

    def withdrawal(self, withdrawalAmount):
        if withdrawalAmount < self.__balance:
            self.__balance -= withdrawalAmount
        else:
            print("Insuficient Funds.")

    def deposit(self, depositAmount):
        self.__balance += depositAmount


def main():
    accounts = []
    for i in range(10):
        accounts.append(Account(i, 100))

    while True:
        id = eval(input("Enter account ID: "))

        if id >= 0 and id <= 9:

            print()
            print("Main menu")
            print("1: check balance")
            print("2: withdraw")
            print("3: deposit")
            print("4: exit")
            print()

            menuChoice = eval(input("Enter a choice: "))
            print()

            while menuChoice != 4:
                if menuChoice == 1:
                    balance = accounts[id].getBalance()
                    print("The balance is ", balance)
                    print()
                    print("Main menu")
                    print("1: check balance")
                    print("2: withdraw")
                    print("3: deposit")
                    print("4: exit")
                    print()
                    menuChoice = eval(input("Enter a choice: "))
                    print()

                elif menuChoice == 2:
                    withdrawalAmount = eval(input("Enter withdrawal amount: "))
                    accounts[id].withdrawal(withdrawalAmount)
                    print()
                    print("Main menu")
                    print("1: check balance")
                    print("2: withdraw")
                    print("3: deposit")
                    print("4: exit")
                    print()
                    menuChoice = eval(input("Enter a choice: "))
                    print()
                elif menuChoice == 3:
                    depositAmount = eval(input("Enter deposit amount: "))
                    accounts[id].deposit(depositAmount)
                    print()
                    print("Main menu")
                    print("1: check balance")
                    print("2: withdraw")
                    print("3: deposit")
                    print("4: exit")
                    print()
                    menuChoice = eval(input("Enter a choice: "))
                    print()
                else:
                    menuChoice = eval(input(("Please enter a valid menu choice (1-4): ")))
                    print()
        else:
            print("Account ID must be a number between 0 and 9. Please try again.")
            print()

main()
