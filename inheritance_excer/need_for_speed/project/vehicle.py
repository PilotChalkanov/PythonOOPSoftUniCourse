
class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self,fuel,horse_power):
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self,kilometers):
        total_consumption = self.fuel_consumption * kilometers
        if total_consumption <= self.fuel:
            self.fuel -= total_consumption
            # return f"Fuel after trip: {self.fuel}\nFuel burned {total_consumption}"
            return self.fuel

# vehicle = Vehicle(50, 150)
# print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
# print(vehicle.fuel)
# print(vehicle.horse_power)
# print(vehicle.fuel_consumption)
# vehicle.drive(100)
# print(vehicle.fuel)