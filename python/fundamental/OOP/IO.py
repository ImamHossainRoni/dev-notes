class MyClass:
    def input(self):
        self.n1 = int(input("First Number = "))
        self.n2 = int(input("Second Number = "))
    def output(self):
        print("Output = "+str(self.n1+self.n2))

obj = MyClass()
obj.input()
obj.output()