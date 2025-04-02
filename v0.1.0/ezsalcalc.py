#python version of ezsalcalc :p this is a minimal viable product
class Workers:  # Class for workers
    def __init__(self, name, id):  # Constructor
        self.name = name
        self.id = id
        self.salary = 0  # Initialize salary to 0

    @staticmethod
    def workerList():  # List of existing workers
        workers = [
            Workers("John", 1),
            Workers("Pjotr", 2),
            Workers("Hans", 3),
            Workers("Johan", 4),
            Workers("Carlito", 5),
            Workers("Miguel", 6)
        ]
        return workers

class GrossPay:
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate
        self.gross = hours * rate

    def grossPay(self):
        return self.gross

def main():
    print("Welcome to EZ Salary Calculator")
    workers = Workers.workerList()

    # Enter hours and rate for each worker
    for worker in workers:
        print(f"\nEnter details for {worker.name} (ID: {worker.id}):")
        hours = float(input("Enter the number of hours worked: "))
        rate = float(input("Enter the hourly rate: "))
        gross = GrossPay(hours, rate)
        worker.salary = gross.grossPay()  # Assign calculated salary to the worker

    # Sort workers by salary in descending order
    workers.sort(key=lambda w: w.salary, reverse=True)

    # Output the salaries for all workers
    print("\nSalaries sorted by gross pay:")
    for worker in workers:
        print(f"Worker's name: {worker.name}, ID: {worker.id}, Gross pay: {worker.salary}")

if __name__ == "__main__":
    main()