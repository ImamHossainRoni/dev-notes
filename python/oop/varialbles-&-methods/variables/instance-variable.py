class Car:
    def __init__(self, brand, color):
        self.brand = brand  # Instance variable
        self.color = color  # Instance variable


car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")

print(car1.brand)
print(car2.color)
