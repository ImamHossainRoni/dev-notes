class Math:
    factor = 2

    @staticmethod
    def multiply(num):
        return num * Math.factor


print(Math.multiply(5))
