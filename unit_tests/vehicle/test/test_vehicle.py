from unittest import main, TestCase
from vehicle.project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(20.5, 100.5)

    def test_vehicle_init(self):

        self.assertEqual(20.5,self.vehicle.fuel)
        self.assertEqual(20.5,self.vehicle.capacity)
        self.assertEqual(100.5, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)


    def test_vehicle_str_should_return_proper_string(self):
        actual = str(self.vehicle)
        expected = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(actual,expected)

    def test_drive_should_rise_error_not_enough_fuel(self):
        max_distance = self.vehicle.fuel/self.vehicle.fuel_consumption

        with self.assertRaises(Exception) as context:
            self.vehicle.drive(max_distance+1)

        self.assertEqual('Not enough fuel', str(context.exception))

    def test_drive_should_decrease_vehicle_fuel(self):

        max_distance = self.vehicle.fuel/self.vehicle.fuel_consumption
        self.vehicle.drive(max_distance)

        self.assertEqual(0, self.vehicle.fuel)


    def test_refuel_should_raise_error_when_cpacity_exceeded(self):

        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(10)

        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual("Too much fuel", str(context.exception))

    def test_refuel_should_increase_amount_of_fuel(self):
        self.vehicle.drive(5)
        fuel_left = self.vehicle.fuel
        refuel_amount = 5
        self.vehicle.refuel(refuel_amount)
        expected_fuel = fuel_left+refuel_amount
        self.assertEqual(expected_fuel,self.vehicle.fuel)


if __name__ == "__main__":
    main()