class BankAccount:
  def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance
    
  def deposit(self,amount):
    self.balance += amount
    print(f"{self.owner} deposited ${amount}. New balance ${self.balance}")
    
  def withdraw (self,amount):
    if amount <= self.balance:
      self.balance -= amount
      print(f"{self.owner} withdrew ${amount}. New balance: ${self.balance}")
    else:
      print("Insufficient funds!")
  
  def showInfo(self):
    return f"{self.owner} balance: ${self.balance}"

accounts =[]

while True:
  print("--Menu--")
  print("1. List Account")
  print("2. Create Account")
  print("3. Deposit")
  print("4. Withdraw")
  print("5. Exit")
  
  menu = input("Select menu:")
  
  if menu =="1":
    for index, account in enumerate(accounts):
      print(f"{index} - {account.showInfo()}")
  
  elif menu =="2":
    name = input("Insert name: ")
    balance = int(input("Insert balance: "))
    accounts.append(BankAccount(name, balance,))
  
  elif menu =="3":
    index = int(input("Choose account index: "))
    amount = int(input("Insert deposit amount: "))
    accounts[index].deposit(amount)
    
  elif menu == "4":
    index = int(input("Choose account index: "))
    amount = int(input("Insert withdraw amount: "))
    accounts[index].withdraw(amount)
  
  elif menu == "5":
    break