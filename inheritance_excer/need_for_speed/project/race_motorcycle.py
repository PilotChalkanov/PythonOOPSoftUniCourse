
from project.motorcycle import Motorcycle

class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8
    def __init__(self,fuel:float,horse_power:int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION


# motor = RaceMotorcycle(160,150)
# print(motor.DEFAULT_FUEL_CONSUMPTION)
# print(motor.drive(20))
