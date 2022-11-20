from project.vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self,fuel,horse_power):
        super().__init__(fuel,horse_power)


# motor = Motorcycle(50,150)
# print(motor.DEFAULT_FUEL_CONSUMPTION)
# print(motor.drive(30))