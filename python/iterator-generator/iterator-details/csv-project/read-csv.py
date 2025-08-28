import csv

with open("customers.csv", "r") as f:
    reader = csv.reader(f)  # reader is an iterator.
    # rows = list(reader)  # loads whole file into memory, not recommended
    # for row in reader:
    #     print(row)

    while True:
        try:
            row = next(reader)
            print(row)
        except StopIteration:
            break
