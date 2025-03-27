class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return "{0} {1}".format(self.brand, self.model)

    @staticmethod
    def sample_information():
        return "It behaves like a regular function but is logically grouped inside a class for better organization."


car1 = Car("BMW", "X1")
print(car1.full_name())
print(car1.sample_information())
