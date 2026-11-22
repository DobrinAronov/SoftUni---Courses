class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class TestIntegerList(TestCase):

    def setUp(self) -> None:
        self.i_ls = IntegerList(0, "5", -3, "abc", 100)

    def test_get_data(self):
        self.assertEqual([0, -3, 100], self.i_ls.get_data())

    def test_add_not_int_type_data(self):
        with self.assertRaises(ValueError) as ex:
            self.i_ls.add("6")
        self.assertEqual("Element is not Integer", str(ex.exception))

        self.assertEqual([0, -3, 100], self.i_ls.get_data())

    def test_add(self):
        self.i_ls.add(-6)
        self.assertEqual([0, -3, 100, -6], self.i_ls.get_data())

    def test_remove_index_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.i_ls.remove_index(100)
        self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual([0, -3, 100], self.i_ls.get_data())

    def test_remove_index(self):
        result = self.i_ls.remove_index(1)

        self.assertEqual(-3, result)
        self.assertEqual([0, 100], self.i_ls.get_data())

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.i_ls.get(30)
        self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual([0, -3, 100], self.i_ls.get_data())

    def test_get(self):
        result = self.i_ls.get(0)
        self.assertEqual(0, result)

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.i_ls.insert(10, 15)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([0, -3, 100], self.i_ls.get_data())

    def test_insert_invalid_type(self):
        with self.assertRaises(ValueError) as ex:
            self.i_ls.insert(0, "15")
        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual([0, -3, 100], self.i_ls.get_data())

    def test_insert(self):
        result = self.i_ls.insert(2, -100)
        self.assertEqual([0, -3, -100, 100], self.i_ls.get_data())

    def test_get_biggest(self):
        result = self.i_ls.get_biggest()
        self.assertEqual(100, result)

    def test_get_index(self):
        result = self.i_ls.get_index(100)
        self.assertEqual(2, result)


if __name__ == "__main__":
    main()
