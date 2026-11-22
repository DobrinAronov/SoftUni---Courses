class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class TestCat(TestCase):

    def setUp(self) -> None:
        self.c = Cat("test_name")

    def test_init(self):
        self.assertEqual(self.c.name, "test_name")
        self.assertFalse(self.c.fed)
        self.assertFalse(self.c.sleepy)
        self.assertEqual(0, self.c.size)

    def test_eat_when_cat_is_fed(self):
        self.c.eat()
        with self.assertRaises(Exception) as ex:
            self.c.eat()
        self.assertEqual('Already fed.', str(ex.exception))

        self.assertTrue(self.c.fed)
        self.assertTrue(self.c.sleepy)
        self.assertEqual(1, self.c.size)

    def test_eat(self):
        self.c.eat()

        self.assertTrue(self.c.fed)
        self.assertTrue(self.c.sleepy)
        self.assertEqual(1, self.c.size)

    def test_sleep_without_eat(self):
        with self.assertRaises(Exception) as ex:
            self.c.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

        self.assertFalse(self.c.fed)
        self.assertFalse(self.c.sleepy)
        self.assertEqual(0, self.c.size)

    def test_sleep(self):
        self.c.eat()
        self.c.sleep()

        self.assertTrue(self.c.fed)
        self.assertFalse(self.c.sleepy)
        self.assertEqual(1, self.c.size)


if __name__ == "__main__":
    main()
