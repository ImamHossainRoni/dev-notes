class Car:
    wheels = 4  # class variable

    def __init__(self, make, model, year, color):
        self.make = make  # instance variable
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This cart is stopped")


car_1 = Car("Chevy", "Corvette", "2021", "blue")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

print(Car.wheels)

