import time

def fetch_data(request_id):
    print(f"Starting request {request_id}")
    time.sleep(1)
    print(f"Finished request {request_id}")
    return f"Data {request_id}"

def main():
    start = time.perf_counter()

    results = [
        fetch_data(i)
        for i in range(1, 6)
    ]

    elapsed = time.perf_counter() - start
    print("Results:", results)
    print(f"Total time: {elapsed:.2f} seconds")

main()