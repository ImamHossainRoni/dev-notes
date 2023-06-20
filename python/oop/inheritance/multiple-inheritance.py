class Engine:
    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")


class ElectricEngine(Engine):
    def start(self):
        print("Electric engine started.")


class CombustionEngine(Engine):
    def start(self):
        print("Combustion engine started.")


class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def drive(self):
        print(f"{self.manufacturer} vehicle is driving.")


class ElectricVehicle(Vehicle, ElectricEngine):
    pass


class HybridVehicle(Vehicle, ElectricEngine, CombustionEngine):
    pass


electric_car = ElectricVehicle("Tesla")
electric_car.start()
electric_car.drive()
electric_car.stop()

print()

hybrid_car = HybridVehicle("Toyota")
hybrid_car.start()
hybrid_car.drive()
hybrid_car.stop()
