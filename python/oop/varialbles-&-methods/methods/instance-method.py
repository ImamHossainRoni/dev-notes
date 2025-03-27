class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return "{0} {1}".format(self.brand, self.model)


car1 = Car("BMW", "X1")
print(car1.full_name())
