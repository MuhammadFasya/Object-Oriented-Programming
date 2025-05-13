class Animal:
    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return "Meow!"

cat = Cat()
print(cat.speak())  # Output: Woof!
