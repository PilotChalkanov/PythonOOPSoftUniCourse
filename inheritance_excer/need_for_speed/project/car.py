from project.vehicle import Vehicle

class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION
        


# fam_car = Car(160,150)
# print(fam_car.DEFAULT_FUEL_CONSUMPTION)
# print(fam_car.drive(10))
