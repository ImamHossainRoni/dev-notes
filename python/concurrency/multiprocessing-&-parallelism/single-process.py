import time

def calculate(start, end):
    total = 0

    for i in range(start, end):

        total += i * i

    return total


if __name__ == "__main__":
    start_time = time.time()

    result = calculate(0, 100_000_000)

    print("Result:", result)
    print("Time:", time.time() - start_time)