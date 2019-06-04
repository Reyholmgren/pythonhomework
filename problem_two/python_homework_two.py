# Write a Class called BankAccount that has 4 methods: getAmountFromConsole, deposit, withdraw, balance
# The getAmountFromConsole method should get user input from the console
# The deposit method should ask for an amount to deposit and update the balance in the account. The withdraw method
# should ask for an amount to withdraw and update the balance in the account. The balance method should print out the
# current balance
# Create an instance of the class and make some calls to prove the class works correctly.


class BankAccount:
    def __init__(self):
        self.starting_balance = 0
        print("Welcome to Vivint bank, let's get started.")

    def deposit(self):
        amount_deposited = float(input("How much are you depositing today?: "))
        self.starting_balance += amount_deposited
        print("\n")
        print("You have deposited: ", amount_deposited)

    def withdraw(self):
        withdrawn_amount = float(input("Enter amount to be Withdrawn: "))
        if self.starting_balance >= withdrawn_amount:
            self.starting_balance -= withdrawn_amount
            print("\n")
            print("You Withdrew: ", withdrawn_amount)
        else:
            print("\n")
            print("You're trying to withdraw more money than you have available")

    def balance(self):
        print("\n")
        print("Current balance is ", self.starting_balance)


# calling class
bank_balance = BankAccount()
# calling methods
bank_balance.deposit()
bank_balance.withdraw()
bank_balance.balance()
