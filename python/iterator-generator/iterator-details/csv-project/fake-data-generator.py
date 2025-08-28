import csv
from faker import Faker

fake = Faker()


def generate_customers(filename: str, total: int):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "age"])

        for i in range(1, total + 1):
            name = fake.first_name()
            age = fake.random_int(min=18, max=80)
            writer.writerow([i, name, age])


generate_customers("customers.csv", 50)

