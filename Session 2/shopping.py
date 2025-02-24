class CartItem:
  def __init__(self,name,price,quantity = 0):
    self.name = name
    self.price = price
    self.quantity = quantity
    
  def addItem(self,quantity):
    self.quantity+= quantity
    print(f"Added {quantity} {self.name} to the cart. Total item: {self.quantity} {self.name}(s)")
  
  def removeItem(self,quantity):
    if quantity > self.quantity:
      print(f"Cannot remove {quantity} {self.name} from the cart. There is only {self.quantity} {self.name} in the cart")
    else:
      self.quantity -= quantity
      print(f"Removed {quantity} {self.name} from the cart. There is {self.quantity} of {self.name}(s) remaining")
  
  def calculateTotal(self):
    return self.quantity * self.price
  def showTotal(self):
    total = self.calculateTotal()
    print(f"You have bought {self.quantity} {self.name} with each of it is ${self.price}, so your total is: ${total:.2f}")

#Object
item1 = CartItem("Laptop",1000,1)
item1.showTotal()

item1.addItem(2)
item1.showTotal()

item1.removeItem(2)
item1.showTotal()