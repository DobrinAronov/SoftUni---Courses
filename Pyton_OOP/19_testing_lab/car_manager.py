class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self) -> None:
        self.c = Car("test_make", "test_model", 10, 100)

    def test_init(self):
        self.assertEqual("test_make", self.c.make)
        self.assertEqual("test_model", self.c.model)
        self.assertEqual(10, self.c.fuel_consumption)
        self.assertEqual(100, self.c.fuel_capacity)
        self.assertEqual(0, self.c.fuel_amount)

    def test_make_setter_none(self):
        with self.assertRaises(Exception) as ex:
            self.c.make = None
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_setter_empty(self):
        with self.assertRaises(Exception) as ex:
            self.c.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_setter(self):
        self.c.make = "abc"
        self.assertEqual("abc", self.c.make)

    def test_setter_model_none(self):
        with self.assertRaises(Exception) as ex:
            self.c.model = None
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_setter_model_empty(self):
        with self.assertRaises(Exception) as ex:
            self.c.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_setter_model(self):
        self.c.model = "xyz"
        self.assertEqual("xyz", self.c.model)

    def test_setter_fuel_consumption_zero(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_setter_fuel_consumption_negative(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption(self):
        self.c.fuel_consumption = 5
        self.assertEqual(5, self.c.fuel_consumption)

    def test_setter_capacity_zero(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_setter_capacity_negative(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_setter_capacity(self):
        self.c.fuel_capacity = 150
        self.assertEqual(150, self.c.fuel_capacity)

    def test_fuel_amount_zero(self):
        self.c.fuel_amount = 0
        self.assertEqual(0, self.c.fuel_amount)

    def test_fuel_amount_negative(self):
        with self.assertRaises(Exception) as ex:
            self.c.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount(self):
        self.c.refuel(300)
        self.assertEqual(100, self.c.fuel_amount)

    def test_refuel_zero(self):
        with self.assertRaises(Exception) as ex:
            self.c.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_negative(self):
        with self.assertRaises(Exception) as ex:
            self.c.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel(self):
        self.c.refuel(50)
        self.assertEqual(50, self.c.fuel_amount)
        self.c.refuel(200)
        self.assertEqual(100, self.c.fuel_amount)

    def test_drive_invalid_distance(self):
        self.c.refuel(100)
        with self.assertRaises(Exception) as ex:
            self.c.drive(1500)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))
        self.assertEqual(100, self.c.fuel_amount)

    def test_drive_valid_distance(self):
        self.c.refuel(10)
        self.c.drive(100)
        self.assertEqual(0, self.c.fuel_amount)


if __name__ == "__main__":
    main()
