class BankAccount:
  def __init__(self, account_holder, balance, pin):
    self.account_holder = account_holder
    self._balance = balance
    self.__pin = pin
  
  def get_balance(self):
    return self._balance
  def set_balance(self, value):
    if value > 0 :
      self._balance = value
    else :
      print("Invalid balance")
  def verify_pin(self, pin):
    return self.__pin == pin
  
# Instances 
account = BankAccount("Ujang", 70000, "12345")

# Access public attributes
print(f"Account of : {account.account_holder}")

# Access protected and private attributes
print(f"Balance: {account._balance}")
# print(f"Pin : {account.__pin}")

# Getter and Setter
print(f"First balance : {account.get_balance()}")

account.set_balance(80000)
print(f"Second balance: {account.get_balance()}")

account.set_balance(-500)

#PIN Verification
print("PIN correct: ", account.verify_pin("12345"))
print("PIN incorrect: ", account.verify_pin("12344"))