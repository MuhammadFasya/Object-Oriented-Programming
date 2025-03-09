class BankAccount:
    def __init__(self, account_number, account_holder, balance, pin):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = balance
        self.__pin = pin

    def deposit(self, amount):
        if amount <= 10000:  # Batas maksimal deposit per transaksi
            self._balance += amount
            print(f"{self.account_holder} deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit limit exceeded! Maximum deposit is $10,000 per transaction.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"{self.account_holder} withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Insufficient funds!")

    def verify_pin(self, pin):
        return self.__pin == pin

    def get_balance(self, pin):
        if self.verify_pin(pin):
            return f"Current balance: ${self._balance}"
        return "Incorrect PIN!"

    def display_account_details(self):
        print(f"Account: {self.account_number} | Holder: {self.account_holder} | Balance: ${self._balance}")


class SavingsAccount(BankAccount):
    WITHDRAW_LIMIT = 500

    def __init__(self, account_number, account_holder, balance, pin):
        super().__init__(account_number, account_holder, balance, pin)

    def withdraw(self, amount):
        if amount > self.WITHDRAW_LIMIT:
            print(f"Cannot withdraw more than ${self.WITHDRAW_LIMIT} per transaction.")
        else:
            super().withdraw(amount)


class PremiumSavingsAccount(SavingsAccount):
    WITHDRAW_LIMIT = 2000

    def __init__(self, account_number, account_holder, balance, pin):
        super().__init__(account_number, account_holder, balance, pin)


# Simulasi Sistem Interaktif
accounts = {}

while True:
    print("\n-- Bank Menu --")
    print("1. List Accounts")
    print("2. Create Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Exit")

    menu = input("Select menu: ")

    if menu == "1":  # List all accounts
        if accounts:
            print("\nList of Accounts:")
            for acc in accounts.values():
                acc.display_account_details()
        else:
            print("\nNo accounts found!")

    elif menu == "2":  # Create account
        acc_number = input("Enter account number: ")
        if acc_number in accounts:
            print("Account number already exists!")
            continue

        acc_holder = input("Enter account holder name: ")
        balance = float(input("Enter initial balance: "))
        pin = input("Set your 4-digit PIN: ")

        print("Select Account Type:")
        print("1. Savings Account (Max withdraw $500 per transaction)")
        print("2. Premium Savings Account (Max withdraw $2000 per transaction)")
        acc_type = input("Choose type (1/2): ")

        if acc_type == "1":
            accounts[acc_number] = SavingsAccount(acc_number, acc_holder, balance, pin)
        elif acc_type == "2":
            accounts[acc_number] = PremiumSavingsAccount(acc_number, acc_holder, balance, pin)
        else:
            print("Invalid account type!")

        print("Account successfully created!")

    elif menu == "3":  # Deposit
        acc_number = input("Enter account number: ")
        if acc_number in accounts:
            amount = float(input("Enter deposit amount: "))
            accounts[acc_number].deposit(amount)
        else:
            print("Account not found!")

    elif menu == "4":  # Withdraw
        acc_number = input("Enter account number: ")
        if acc_number in accounts:
            pin = input("Enter PIN: ")
            if accounts[acc_number].verify_pin(pin):
                amount = float(input("Enter withdrawal amount: "))
                accounts[acc_number].withdraw(amount)
            else:
                print("Incorrect PIN!")
        else:
            print("Account not found!")

    elif menu == "5":  # Check balance
        acc_number = input("Enter account number: ")
        if acc_number in accounts:
            pin = input("Enter PIN: ")
            print(accounts[acc_number].get_balance(pin))
        else:
            print("Account not found!")

    elif menu == "6":  # Exit
        print("Thank you for using our banking service!")
        break

    else:
        print("Invalid option! Please choose a valid menu option.")
