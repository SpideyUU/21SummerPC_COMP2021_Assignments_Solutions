import sys


class Account:
    def __init__(self):
        self.__balance = 100.0
        self.__id = 0
        self.__annualInterestRate = 0.0

    def getMonthlyInterestRate(self):
        return (self.annualInterestRate / 100) / 12

    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()

    def withdraw(self, amount):
        self.__balance = self.__balance - amount

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def getBalance(self):
        return self.__balance


def getMainMenu():
    return "Main menu \n1: Check balance \n2: Withdraw \n3: Deposit \n4: Exit \nEnter a choice: "


class ATM_machine(Account):
    def __init__(self, user_id):
        super().__init__()
        self.id = user_id


def main():
    account = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    while True:
        id1 = eval(input("Enter an account id: "))
        if id1 in account:
            atm_machine = ATM_machine(id1)
            while True:
                choice_input = eval(input(getMainMenu()))
                if choice_input == 1:

                    print("The balance is: ", atm_machine.getBalance())
                    getMainMenu()
                elif choice_input == 2:
                    d = eval(input("Enter an amount to withdraw: "))
                    atm_machine.withdraw(d)
                    getMainMenu()
                elif choice_input == 3:
                    d = eval(input("Enter an amount to Deposit: "))
                    atm_machine.deposit(d)
                    getMainMenu()
                elif choice_input == 4:
                    sys.exit()
                    break
        else:
            print("Incorrect account id!")
        continue


main()
