import unittest
from student import *

class TestStudent(unittest.TestCase):

    def setUp(self):
        students.clear()

    def test_add_student(self):
        self.assertTrue(add_student(1, "Alice"))
        self.assertFalse(add_student(1, "Bob"))

    def test_search_student(self):
        add_student(1, "Alice")
        self.assertEqual(search_student(1), "Alice")

    def test_update_student(self):
        add_student(1, "Alice")
        self.assertTrue(update_student(1, "Bob"))
        self.assertEqual(search_student(1), "Bob")

    def test_remove_student(self):
        add_student(1, "Alice")
        self.assertTrue(remove_student(1))
        self.assertIsNone(search_student(1))

if __name__ == "__main__":
    unittest.main()