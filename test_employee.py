""" Good Pratice: each are isolated and independents."""
import unittest
from unittest.mock import patch

from employee import Employee


class TestEmployee(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self) -> None:
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50_000)
        self.emp_2 = Employee('Sue', 'Smith', 60_000)
    
    def tearDown(self) -> None:
        print('tearDown')
        
    def test_email(self):
        print('test_email\n')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')
        
    def test_fullname(self):
        print('test_fullname')
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    
    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52_500)
        self.assertEqual(self.emp_2.pay, 63_000)


    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('https://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False
            
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('https://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')            

if __name__ == '__main__':
    unittest.main()