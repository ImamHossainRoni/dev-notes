import threading
import time


def process_order(order_id):
    print(f"Processing order {order_id}...")
    time.sleep(2)
    print(f"Order {order_id} is ready!")


orders = [1, 2, 3, 4, 5]
threads = []

for order in orders:
    t = threading.Thread(target=process_order, args=(order,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All orders processed!")
