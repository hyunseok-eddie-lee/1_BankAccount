# Create a BankAccount class with the attributes interest rate and balance
class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

# Add a deposit method to the BankAccount class
# deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        return self

# Add a withdraw method to the BankAccount class
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; 
# if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

# Add a display_account_info method to the BankAccount class
# display_account_info(self) - print to the console: eg. "Balance: $100"

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

# Add a yield_interest method to the BankAccount class
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info

    @classmethod
    def print_all_accounts(cls):
        for all_accounts in cls.all_accounts:
            all_accounts.display_account_info()


# Create 2 accounts

checking_account = BankAccount(0.01, 6000)
saving_account = BankAccount(0.03, 2000)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)

checking_account.deposit(3000).deposit(3300).deposit(3600).withdraw(6000).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)

saving_account.deposit(1900).deposit(2000).withdraw(300).withdraw(330).withdraw(360).withdraw(390).yield_interest().display_account_info()


BankAccount.print_all_accounts()