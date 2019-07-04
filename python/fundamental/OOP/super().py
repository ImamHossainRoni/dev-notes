class A:
    def __init__(self):
        print('in A')
    def a(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print('in B')
    def b(self):
        print("B")

obj = B()
