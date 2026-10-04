class Car:
    wheels = 4  #cls variable
    def __init__(self):
        # Instance variable
        self.name = "BMW"
        self.mil = 100

obj1 =Car()
print(obj1.name, obj1.mil)
print(obj1.wheels)