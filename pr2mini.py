# Bank Management System

class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(
                f"Deposited Rs {amount} now!! Congrats!! "
                f"Your account has balance Rs {self.__balance}"
            )
        else:
            print(
                "Invalid amount. Please try again or wait for some minutes "
                "if already debited from account."
            )

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Your account may not have such amount. Please try again later.")

        elif amount <= 0:
            print("You have entered 0 or an invalid amount. Please try again!")

        else:
            self.__balance -= amount
            print(f"Rs {amount} withdrawn successfully.")

    def show_balance(self):
        print(f"Hi {self.name}, your balance is: Rs {self.__balance}")


#objects
BankAccount1 = BankAccount("barbiedoll", 2000)

BankAccount1.show_balance()
BankAccount1.deposit(500)
BankAccount1.withdraw(1000)
BankAccount1.show_balance()
BankAccount2= BankAccount("shipra",10000000000000000)
BankAccount2.show_balance()

       
    
       