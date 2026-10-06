import time
from multiprocessing import Process, Queue


def calculate(start, end, result_queue):
    total = 0

    for i in range(start, end):
        total += i * i

    result_queue.put(total)

    print(f"Finished: {start} - {end}")


if __name__ == "__main__":

    start_time = time.time()

    result_queue = Queue()

    p1 = Process(
        target=calculate,
        args=(0, 25_000_000, result_queue)
    )

    p2 = Process(
        target=calculate,
        args=(25_000_000, 50_000_000, result_queue)
    )

    p3 = Process(
        target=calculate,
        args=(50_000_000, 75_000_000, result_queue)
    )

    p4 = Process(
        target=calculate,
        args=(75_000_000, 100_000_000, result_queue)
    )

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    # Wait for processes
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    total = 0

    for _ in range(4):
        total += result_queue.get()

    print("Total:", total)
    print("Time:", time.time() - start_time)