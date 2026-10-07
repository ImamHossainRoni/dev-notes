import time
from concurrent.futures import ProcessPoolExecutor

def calculate(args):
    start, end = args
    total = 0
    for i in range(start, end):
        total += i * i

    print(f"Finished: {start} - {end}")
    return total


if __name__ == "__main__":
    start_time = time.time()
    ranges = [
        (0, 25_000_000),
        (25_000_000, 50_000_000),
        (50_000_000, 75_000_000),
        (75_000_000, 100_000_000),
    ]

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(calculate, ranges)
        total = sum(results)

    print("Total:", total)
    print("Time:", time.time() - start_time)