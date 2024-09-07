import unittest
from student import Student



class TestStudent(unittest.TestCase):
    
    def test_student_full_name(self):
        student = Student("john", "bobby")
        self.assertEqual(student.full_name, "John Bobby")


if __name__ == "__main__":
    unittest.main()