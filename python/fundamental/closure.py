def make_total():
    arr = []

    def get_total(value):
        arr.append(value)
        return sum(arr)
    return get_total

sum1 = make_total

print(sum1(10))
print(sum1(10))
print(sum1(10))
print(sum1(10))
print(sum1(10))