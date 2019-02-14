class Person:
    def __init__(self):
        self.name = "Roni"
        self.age =23

    def update(self):
        self.name = "Imam"
        self.age = 25
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
c1 = Person()
c2 = Person()
c1.update()
if c1.compare(c2):
    print("They are same")
else:
    print("They are not same")
print(c1.age)
print(c2.name)