class Calculator:
    def __init__(self,n1,n2):
        self._n1 = n1
        self._n2 = n2
    def add(self):
        return self._n1+self._n2
    def sub(self):
        if self._n1 > self._n2:
            return  self._n1 - self._n2
        else:
            return "First number should be greater"
    def mul(self):
        return self._n1*self._n2
    def div(self):
        if self._n1 > self._n2:
            return self._n1/self._n2
        else:
            return "First number should be greater"

obj = Calculator(10,5)
print(obj.add())
print(obj.sub())
print(obj.mul())
print(obj.div())