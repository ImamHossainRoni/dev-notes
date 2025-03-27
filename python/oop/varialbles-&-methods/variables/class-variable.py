class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

    @classmethod
    def change_wheels(cls, new_count):
        cls.wheels = new_count

    def new_wheels(self):
        self.wheels = 90


car = Car("TESLA")
car.new_wheels()
# Car.change_wheels(6)
# Car.wheels = 30
print(Car.wheels)
