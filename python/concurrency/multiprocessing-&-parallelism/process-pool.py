from concurrent.futures import ProcessPoolExecutor
import time


def process_data(number):
    total = 0
    for i in range(10_000_000):
        total += (i * number) ** 2
    return total


if __name__ == "__main__":

    start = time.perf_counter()

    numbers = range(1, 9)

    with ProcessPoolExecutor(max_workers=4) as executor:

        results = executor.map(process_data, numbers)

    print(list(results))

    print("Time:", time.perf_counter() - start)