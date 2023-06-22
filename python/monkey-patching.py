"""
    Monkey patching in Python refers to the technique of modifying or extending the behavior of existing code at
    runtime, typically by adding, replacing, or modifying attributes or methods of an existing class or object.
"""


class Power:
    def square(self, num):
        return f"The square of {num} is {num ** 2}"


def cube(self, num):
    return f"The cube of {num} is {num ** 3}"


power = Power()
Power.square = cube  # Monkey pathing
print(power.square(2))
