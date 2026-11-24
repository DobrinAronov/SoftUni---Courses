from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    fuel = 50.3
    horse_power = 153.7

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_init_type(self):
        self.assertIsInstance(self.fuel, float)
        self.assertIsInstance(self.vehicle.capacity, float)
        self.assertIsInstance(self.horse_power, float)
        self.assertIsInstance(self.vehicle.fuel_consumption, float)

    def test_init(self):
        self.assertEqual(50.3, self.fuel)
        self.assertEqual(50.3, self.vehicle.capacity)
        self.assertEqual(153.7, self.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)
        self.assertEqual("Not enough fuel", str(ex.exception))

        self.assertEqual(50.3, self.vehicle.fuel)

    def test_drive_with_enough_fuel(self):
        self.vehicle.drive(5)
        self.assertEqual(44.05, self.vehicle.fuel)

    def test_refuel_over_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

        self.assertEqual(50.3, self.vehicle.fuel)

    def test_refuel_success(self):
        self.vehicle.fuel = 10
        self.vehicle.refuel(35.5)
        self.assertEqual(45.5, self.vehicle.fuel)

    def test_str(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
                   f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"

        self.assertEqual(expected, str(self.vehicle))


if __name__ == "__main__":
    main()
