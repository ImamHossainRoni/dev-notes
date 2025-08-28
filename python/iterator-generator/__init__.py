import time

N = 1_000_000

# List comprehension
start = time.perf_counter()
nums_list = [i * i for i in range(N)]
for i in nums_list[:3]:
    print("From list:", i)
end = time.perf_counter()
print("List time:", end - start)

# Generator
start = time.perf_counter()
nums_gen = (i * i for i in range(N))
for i, v in enumerate(nums_gen):
    if i < 3:
        print("From generator:", v)
    else:
        break
end = time.perf_counter()
print("Generator time:", end - start)

