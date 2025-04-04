import unittest
from unittest.mock import patch
from ezsalcalc import Workers, WorkerRegistry, HRDepartment, GrossPay

class TestEzSalaryCalculator(unittest.TestCase):

    def setUp(self):
        # Reset the worker list to its initial state before each test
        WorkerRegistry._worker_list = [
            Workers("John", 1),
            Workers("Pjotr", 2),
            Workers("Hans", 3),
            Workers("Johan", 4),
            Workers("Carlito", 5),
            Workers("Miguel", 6)
        ]

    def test_worker_initialization(self):
        # Positive case
        worker = Workers("John", 1)
        self.assertEqual(worker.name, "John")
        self.assertEqual(worker.id, 1)
        self.assertEqual(worker.salary, 0)  # Ensure salary is initialized to 0
        
        # Negative case
        with self.assertRaises(TypeError):
            Workers("John")  # Missing ID
        with self.assertRaises(TypeError):
            Workers()  # Missing name and ID

    def test_worker_list(self):
        workers = WorkerRegistry.workerList()
        self.assertEqual(len(workers), 6)
        self.assertEqual(workers[0].name, "John")
        self.assertEqual(workers[1].name, "Pjotr")
        self.assertTrue(all(worker.salary == 0 for worker in workers))  # Ensure all salaries are 0 initially

    def test_gross_pay_calculation(self):
        # Positive case
        gross_pay = GrossPay(40, 15)
        self.assertEqual(gross_pay.grossPay(), 600)
        
        # Negative case
        gross_pay = GrossPay(0, 15)
        self.assertEqual(gross_pay.grossPay(), 0)
        gross_pay = GrossPay(40, 0)
        self.assertEqual(gross_pay.grossPay(), 0)

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

    def test_salary_assignment_and_sorting(self):
        workers = WorkerRegistry.workerList()
        
        # Assign salaries to workers
        workers[0].salary = GrossPay(40, 15).grossPay()  # John: 600
        workers[1].salary = GrossPay(35, 20).grossPay()  # Pjotr: 700
        workers[2].salary = GrossPay(50, 10).grossPay()  # Hans: 500
        
        # Sort workers by salary in descending order
        workers.sort(key=lambda w: w.salary, reverse=True)
        
        # Verify sorting
        self.assertEqual(workers[0].name, "Pjotr")  # Highest salary
        self.assertEqual(workers[1].name, "John")
        self.assertEqual(workers[2].name, "Hans")

    @patch('builtins.input', side_effect=["NewWorker", "7"])
    def test_add_worker(self, mock_input):
        # Positive case: Test adding a worker
        HRDepartment.addWorker()
        workers = WorkerRegistry.workerList()
        self.assertEqual(len(workers), 7)  # Ensure the worker list has increased
        self.assertEqual(workers[-1].name, "NewWorker")  # Check the last worker's name
        self.assertEqual(workers[-1].id, 7)  # Check the last worker's ID

        # Negative case: Test adding a worker with invalid input
        with patch('builtins.input', side_effect=["", ""]):  # Empty name and ID
            with self.assertRaises(ValueError):
                HRDepartment.addWorker()

    @patch('builtins.input', side_effect=["0"])
    def test_remove_worker(self, mock_input):
        # Positive case: Test removing a worker
        HRDepartment.removeWorker()
        workers = WorkerRegistry.workerList()
        self.assertEqual(len(workers), 5)  # Ensure the worker list has decreased
        self.assertNotEqual(workers[0].name, "John")  # Ensure the first worker was removed

        # Negative case: Test removing a worker with invalid input
        with patch('builtins.input', side_effect=["999"]):  # Non-existent worker ID
            with self.assertRaises(ValueError):
                HRDepartment.removeWorker()

if __name__ == "__main__":
    unittest.main()