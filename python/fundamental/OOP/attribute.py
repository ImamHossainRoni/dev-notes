class Computer:
    def __init__(self,ram,cpu):
        self.ram = ram
        self.cpu = cpu

    def config(self):
        print(self.cpu,self.ram)
comp1 = Computer('i5','16gb')
comp2 = Computer('i3','4gb')
comp1.config()
comp2.config()