class Car:
  def __init__(self,brand,model,year):
    self.brand = brand
    self.model= model
    self.year = year
    
  def display_info(self):
    print(f"{self.brand} released the {self.model} in {self.year}")
    
# Object
cars = [
Car('Toyota','Avanza','2010'),
Car('Mitshubishi','Pajero','2020'),
Car('Lamborgini','Aventador','2012')
]

for car in cars:
  car.display_info()