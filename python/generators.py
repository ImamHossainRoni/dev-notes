# Iterator & Iterable

nums = [1, 2, 3, 4, 5]

iter_obj = iter(nums)

# print(iter)

# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))


# Generator
"""
    A normal function to return a sequence will create the entire sequence in memory before returning the result. This 
    is an overkill, if the number of items in the sequence is very large.
    
    Generator implementation of such sequences is memory friendly and is preferred since it only produces one item at a 
    time.
"""


def num_gen(n):
    for i in range(1, n + 1):
        yield i


numbers = num_gen(5)

for i in numbers:
    print(i)

for t in numbers:
    print(t)
