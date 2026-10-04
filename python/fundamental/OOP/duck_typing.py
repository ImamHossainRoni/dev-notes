class PyCharm:
    def execute(self):
        print('PyCharm is running!')

class Eclipse:
    def execute(self):
        print('Eclipse is running!')
class Laptop:
    def code(self,ide):
        ide.execute()

ide1 = PyCharm()
ide2 = Eclipse()
laptop = Laptop()

laptop.code(ide1)
laptop.code(ide2)

