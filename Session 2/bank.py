# Bank Account System
# Class: BandAccount
# Attributes: owner_name, balance, accounte_number
# Methods:

class AccountSystem:
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
      
# Creating an account
account1 = AccountSystem("John Dod", 1000)
account1.deposit(500)
account1.withdraw(300)