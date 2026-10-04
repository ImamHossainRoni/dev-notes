class Student:

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "Dell"
            self.os = "Linux"
        def show(self):
            print(self.brand, self.os)

obj1 = Student("Imam",1)
obj1.show()
# obj = Student.Laptop()
# print(obj.show())