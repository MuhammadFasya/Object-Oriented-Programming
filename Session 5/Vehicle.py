class Car:
    def move(self):
      return "Moving with four wheels"
class Bicycle:
    def move(self):
      return "Moving with two wheels"
class Boat:
    def move(self):
      return "Moving on water"
    
def move_vehicle(vehicle):
    print(vehicle.move())

move_vehicle(Car())
move_vehicle(Bicycle())
move_vehicle(Boat())
