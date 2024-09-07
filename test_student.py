import unittest
from student import Student



class TestStudent(unittest.TestCase):
    
    def test_student_full_name(self):
        student = Student("john", "bobby")
        self.assertEqual(student.full_name, "John Bobby")

    def test_alert_santa_return_True(self):
        student = Student("mustafa", "akbari")
        student.alert_santa()
        self.assertTrue(student.naughty_list)
    

    def test_email(self):
        student = Student("john", "bobby")
        self.assertEqual(student.email, "john.bobby@gmail.com")



if __name__ == "__main__":
    unittest.main()