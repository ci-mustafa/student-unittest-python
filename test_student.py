import unittest
from student import Student
from datetime import timedelta




class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("john", "bobby")

    
    def test_student_full_name(self):
        self.assertEqual(self.student.full_name, "John Bobby")


    def test_alert_santa_return_True(self):
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)
    

    def test_email(self):
        self.assertEqual(self.student.email, "john.bobby@gmail.com")
    
    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(days=10)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=10))



if __name__ == "__main__":
    unittest.main()