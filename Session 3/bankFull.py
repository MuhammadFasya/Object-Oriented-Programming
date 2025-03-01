class BankAccount:
    def __init__(self, account_holder, balance, pin):
        self.account_holder = account_holder
        self._balance = balance
        self.__pin = pin

    def get_balance(self, pin):
        if self.verify_pin(pin):
            return f"Current balance: ${self._balance}"
        return "Incorrect PIN!"

    def set_balance(self, pin, value):
        if self.verify_pin(pin):
            if value > 0:
                self._balance = value
            else:
                print("Invalid balance!")
        else:
            print("Incorrect PIN!")

    def verify_pin(self, pin):
        return self.__pin == pin

    def deposit(self, pin, amount):
        if self.verify_pin(pin):
            self._balance += amount
            print(f"{self.account_holder} deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Incorrect PIN!")

    def withdraw(self, pin, amount):
        if self.verify_pin(pin):
            if amount <= self._balance:
                self._balance -= amount
                print(f"{self.account_holder} withdrew ${amount}. New balance: ${self._balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Incorrect PIN!")

    def show_info(self, pin):
        if self.verify_pin(pin):
            return f"{self.account_holder}'s balance: ${self._balance}"
        return "Incorrect PIN!"



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

    if menu == "1":  # List all account
        if accounts:
            print("\nList of Accounts:")
            for name in accounts:
                print(f"- {name}")
        else:
            print("\nNo accounts found!")

    elif menu == "2":  # Create account
        name = input("Enter account holder name: ")
        balance = int(input("Enter initial balance: "))
        pin = input("Set your 4-digit PIN: ")
        if name in accounts:
            print("Account already exists!")
        else:
            accounts[name] = BankAccount(name, balance, pin)
            print("Account successfully created!")

    elif menu == "3":  # Deposit
        name = input("Enter account holder name: ")
        if name in accounts:
            pin = input("Enter PIN: ")
            amount = int(input("Enter deposit amount: "))
            accounts[name].deposit(pin, amount)
        else:
            print("Account not found!")

    elif menu == "4":  # Withdraw
        name = input("Enter account holder name: ")
        if name in accounts:
            pin = input("Enter PIN: ")
            amount = int(input("Enter withdrawal amount: "))
            accounts[name].withdraw(pin, amount)
        else:
            print("Account not found!")

    elif menu == "5":  # Checking balance
        name = input("Enter account holder name: ")
        if name in accounts:
            pin = input("Enter PIN: ")
            print(accounts[name].get_balance(pin))
        else:
            print("Account not found!")

    elif menu == "6":  # Exit
        print("Thank you for using our banking service!")
        break

    else:
        print("Invalid option! Please choose a valid menu option.")
