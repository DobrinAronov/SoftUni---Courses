class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class TestWorker(TestCase):

    def setUp(self) -> None:
        self.w = Worker("test_name", 1000, 10)

    def test_init(self):
        self.assertEqual("test_name", self.w.name)
        self.assertEqual(1000, self.w.salary)
        self.assertEqual(10, self.w.energy)
        self.assertEqual(0, self.w.money)

    def test_work_with_zero_or_negative_energy(self):
        w = Worker("test_name", 1000, 0)
        with self.assertRaises(Exception) as ex:
            w.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

        w.energy = -1
        with self.assertRaises(Exception) as ex:
            w.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work(self):
        self.assertEqual(0, self.w.money)
        self.assertEqual(10, self.w.energy)
        self.w.work()
        self.assertEqual(1000, self.w.money)
        self.assertEqual(9, self.w.energy)

    def test_rest(self):
        self.w.rest()
        self.assertEqual(11, self.w.energy)

    def test_get_info(self):
        self.w.work()
        result = self.w.get_info()
        self.assertEqual('test_name has saved 1000 money.', result)

    def test_work_twice(self):
        self.w.work()
        self.w.work()

        self.assertEqual(2000, self.w.money)
        self.assertEqual(8, self.w.energy)


if __name__ == '__main__':
    main()
