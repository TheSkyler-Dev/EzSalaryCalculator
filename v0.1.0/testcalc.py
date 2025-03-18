import unittest
from ezsalcalc import Worker, GrossPay

class TestEzSalaryCalculator(unittest.TestCase):

    def test_worker_initialization(self):
        # Positive case
        worker = Worker("John", 1)
        self.assertEqual(worker.name, "John")
        self.assertEqual(worker.id, 1)
        
        # Negative case
        with self.assertRaises(TypeError):
            Worker("John")  # Missing ID
        with self.assertRaises(TypeError):
            Worker()  # Missing name and ID

    def test_worker_list(self):
        workers = Worker.worker_list()
        self.assertEqual(len(workers), 6)
        self.assertEqual(workers[0].name, "John")
        self.assertEqual(workers[1].name, "Pjotr")

    def test_gross_pay_calculation(self):
        # Positive case
        gross_pay = GrossPay(40, 15)
        self.assertEqual(gross_pay.calculate_gross_pay(), 600)
        
        # Negative case
        gross_pay = GrossPay(0, 15)
        self.assertEqual(gross_pay.calculate_gross_pay(), 0)
        gross_pay = GrossPay(40, 0)
        self.assertEqual(gross_pay.calculate_gross_pay(), 0)

    def test_gross_pay_initialization(self):
        # Positive case
        gross_pay = GrossPay(40, 15)
        self.assertEqual(gross_pay.hours, 40)
        self.assertEqual(gross_pay.rate, 15)
        self.assertEqual(gross_pay.gross, 600)
        
        # Negative case
        with self.assertRaises(TypeError):
            GrossPay(40)  # Missing rate
        with self.assertRaises(TypeError):
            GrossPay()  # Missing hours and rate

if __name__ == "__main__":
    unittest.main()