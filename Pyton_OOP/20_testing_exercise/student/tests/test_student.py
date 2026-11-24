from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student_1 = Student("student_name_1", {"Python": ["n1", "n2"],
                                                    "JS": ["n3", "n4"]})
        self.student_2 = Student("student_name_2", None)

    def test_init(self):
        self.assertEqual("student_name_1", self.student_1.name)
        self.assertEqual({}, self.student_2.courses)
        expected = {"Python": ["n1", "n2"], "JS": ["n3", "n4"]}
        self.assertEqual(expected, self.student_1.courses)

    def test_enroll_course_exist_in_Courses(self):
        result = self.student_1.enroll("Python", ["n3", "n4"], "")
        self.assertEqual("Course already added. Notes have been updated.", result)
        expected = {"Python": ["n1", "n2", "n3", "n4"], "JS": ["n3", "n4"]}
        self.assertEqual(expected, self.student_1.courses)

    def test_enroll_course_does_not_exist_add_course_notes_is_empty(self):
        result = self.student_2.enroll("Java", ["n1", "n2"], "")
        self.assertEqual("Course and course notes have been added.", result)

        expected = {"Java": ["n1", "n2"]}
        self.assertEqual(expected, self.student_2.courses)

    def test_enroll_course_does_not_exist_add_course_notes_is_Y(self):
        result = self.student_2.enroll("Java", ["n1", "n2"], "Y")
        self.assertEqual("Course and course notes have been added.", result)

        expected = {"Java": ["n1", "n2"]}
        self.assertEqual(expected, self.student_2.courses)

    def test_enroll_success(self):
        result = self.student_1.enroll("Java", ["n1", "n2"], "abc")
        self.assertEqual("Course has been added.", result)
        expected = {"Python": ["n1", "n2"], "JS": ["n3", "n4"], "Java": []}
        self.assertEqual(expected, self.student_1.courses)

    def test_add_notes_course_exist(self):
        result = self.student_1.add_notes("JS", "n5")
        self.assertEqual("Notes have been updated", result)

        expected = {"Python": ["n1", "n2"], "JS": ["n3", "n4", "n5"]}
        self.assertEqual(expected, self.student_1.courses)

    def test_add_notes_course_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.add_notes("Java", "n1")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

        expected = {"Python": ["n1", "n2"], "JS": ["n3", "n4"]}
        self.assertEqual(expected, self.student_1.courses)

    def test_leave_course_when_the_course_exist(self):
        result = self.student_1.leave_course("JS")
        self.assertEqual("Course has been removed", result)

        expected = {"Python": ["n1", "n2"]}
        self.assertEqual(expected, self.student_1.courses)

    def test_leave_course_when_the_course_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.leave_course("Java")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

        expected = {"Python": ["n1", "n2"], "JS": ["n3", "n4"]}
        self.assertEqual(expected, self.student_1.courses)


if __name__ == "__main__":
    main()
