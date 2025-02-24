class Books:
  def __init__(self, title, author, ISBN):
    self.title = title
    self.author = author
    self.isbn = ISBN
    self.available = True
    
  def displayBookAvailability(self):
    status = "Available" if self.available else "Not available"
    print(f"Book:{self.title}, Author:{self.author}, ISBN number: {self.isbn}, availability: {status}")
    
  def borrowingBook(self):
    if self.available:
      self.available = False
      print(f"The book {self.title} has been borrowed")
    else:
      print(f"Sorry, the book {self.title} was not available")
      
  def returnBook(self):
    if not self.available:
      self.available = True
      print(f"The book {self.title} has been returned and now available")
    else:
      print(f"The book {self.title} was not borrowed")
      
#Object
book1 = Books("Introduction to Python","John Mccarty","1298371869")
book1.displayBookAvailability()

# Borrowing
book1.borrowingBook()
book1.displayBookAvailability()

# Returning
book1.returnBook()
book1.displayBookAvailability