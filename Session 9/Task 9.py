# Custom error classes
class InsufficientBalanceError(Exception):
    pass

class AccountNotFoundError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class AuthenticationError(Exception):
    pass

# Bank account class
class BankAccount:
    def __init__(self, username, pin, balance):
        self.username = username
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print(f"[{self.username}] Current balance: Rp {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance for withdrawal.")
        self.balance -= amount
        print(f"Rp {amount} withdrawn. Remaining balance: Rp {self.balance}")

    def transfer(self, target_account, amount):
        if not isinstance(target_account, BankAccount):
            raise AccountNotFoundError("Target account not found.")
        if amount <= 0:
            raise InvalidAmountError("Transfer amount must be greater than zero.")
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance for transfer.")

        self.balance -= amount
        target_account.balance += amount
        print(f"Successfully transferred Rp {amount} to [{target_account.username}].")

# Login system
def login(accounts, input_username, input_pin):
    for account in accounts:
        if account.username == input_username and account.pin == input_pin:
            print(f"Login successful. Welcome, {input_username}!")
            return account
    raise AuthenticationError("Invalid username or PIN.")

# Main program
if __name__ == "__main__":
    # Sample user accounts
    user1 = BankAccount("james", "1234", 500_000)
    user2 = BankAccount("moriarty", "4321", 250_000)

    all_accounts = [user1, user2]

    try:
        # Simulate login
        username_input = input("Enter username: ")
        pin_input = input("Enter PIN: ")

        current_user = login(all_accounts, username_input, pin_input)

        # Sample interactions
        current_user.check_balance()

        # Withdraw
        try:
            amount = int(input("Enter amount to withdraw: "))
            current_user.withdraw(amount)
        except (InvalidAmountError, InsufficientBalanceError) as e:
            print("Withdraw error:", e)

        # Transfer
        try:
            target_username = input("Enter recipient username: ")
            target_account = next((acc for acc in all_accounts if acc.username == target_username), None)
            if not target_account:
                raise AccountNotFoundError("Target account not found.")

            transfer_amount = int(input("Enter amount to transfer: "))
            current_user.transfer(target_account, transfer_amount)
        except (InvalidAmountError, InsufficientBalanceError, AccountNotFoundError) as e:
            print("Transfer error:", e)

    except AuthenticationError as e:
        print("Login failed:", e)
