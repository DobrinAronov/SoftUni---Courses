from project.senior_student import SeniorStudent

from unittest import TestCase, main


class TestSeniorStudent(TestCase):
    def setUp(self) -> None:
        self.student = SeniorStudent("1234", "test_name", 2.4)

    def test_init_type_data(self):
        self.assertIsInstance(self.student.student_id, str)
        self.assertIsInstance(self.student.name, str)
        self.assertIsInstance(self.student.student_gpa, float)
        self.assertIsInstance(self.student.colleges, set)

    def test_init(self):
        self.assertEqual("1234", self.student.student_id)
        self.assertEqual("test_name", self.student.name)
        self.assertEqual(2.4, self.student.student_gpa)
        self.assertEqual(set(), self.student.colleges)

    def test_student_id_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.student.student_id = "123"
        self.assertEqual("Student ID must be at least 4 digits long!", str(ex.exception))
        self.assertEqual("1234", self.student._SeniorStudent__student_id)

    def test_name_setter_name_is_empty(self):
        with self.assertRaises(ValueError) as ex:
            self.student.name = ""
        self.assertEqual("Student name cannot be null or empty!", str(ex.exception))
        self.assertEqual("test_name", self.student._SeniorStudent__name)

    def test_name_setter_name_has_only_spaces(self):
        with self.assertRaises(ValueError) as ex:
            self.student.name = "   "
        self.assertEqual("Student name cannot be null or empty!", str(ex.exception))
        self.assertEqual("test_name", self.student._SeniorStudent__name)

    def test_setter_gta_equal_one(self):
        with self.assertRaises(ValueError) as ex:
            self.student.student_gpa = 1.0
        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))
        self.assertEqual(2.4, self.student.student_gpa)

    def test_setter_gta_less_one(self):
        with self.assertRaises(ValueError) as ex:
            self.student.student_gpa = 0.9
        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))
        self.assertEqual(2.4, self.student.student_gpa)

    def test_apply_to_college_unsuccess(self):
        result = self.student.apply_to_college(2.41, "new_name")
        self.assertEqual('Application failed!', result)
        self.assertEqual(set(), self.student.colleges)

    def test_apply_to_college_success(self):
        result = self.student.apply_to_college(2.39, "new_name")
        expected = f'{self.student.name} successfully applied to new_name.'
        self.assertEqual(expected, result)
        self.assertEqual({'NEW_NAME'}, self.student.colleges)

    def test_update_gpa_unsuccess_new_gpa_equal_one(self):
        result = self.student.update_gpa(1)
        self.assertEqual('The GPA has not been changed!', result)
        self.assertEqual(2.4, self.student.student_gpa)

    def test_update_gpa_unsuccess_new_gpa_less_one(self):
        result = self.student.update_gpa(0.99)
        self.assertEqual('The GPA has not been changed!', result)
        self.assertEqual(2.4, self.student.student_gpa)

    def test_update_gpa_success(self):
        result = self.student.update_gpa(1.01)
        self.assertEqual('Student GPA was successfully updated.', result)
        self.assertEqual(1.01, self.student.student_gpa)

    def test_eq_false(self):
        other = SeniorStudent("5678", "new_name", 2.39)
        result = self.student.__eq__(other)
        self.assertFalse(result)

    def test_eq_true(self):
        other = SeniorStudent("5678", "new_name", 2.4)
        result = self.student.__eq__(other)
        self.assertTrue(result)


if __name__ == "__main__":
    main()
