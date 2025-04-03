#python version of ezsalcalc :p this is a minimal viable product
class Workers:  # Class for workers
    def __init__(self, name, id):  # Constructor
        self.name = name
        self.id = id
        self.salary = 0  # Initialize salary to 0

class WorkerRegistry: # container for all workers
    _worker_list = [
            Workers("John", 1),
            Workers("Pjotr", 2),
            Workers("Hans", 3),
            Workers("Johan", 4),
            Workers("Carlito", 5),
            Workers("Miguel", 6)
        ]

    @staticmethod
    def workerList():  # List of existing workers
        return WorkerRegistry._worker_list
        
class HRDepartment:  # HR class
    @staticmethod
    def addWorker():
        # Add worker to WorkerRegistry's list
        name = input("Enter the new worker's name: ")
        id = int(input("Enter the new worker's ID: "))
        WorkerRegistry._worker_list.append(Workers(name, id))  # Add to the correct list
        print("\nUpdated Worker List:")
        for worker in WorkerRegistry._worker_list:
            print(f"{worker.name}, {worker.id}")

    @staticmethod
    def removeWorker():
        # Display the current worker list with indices
        print("\nCurrent Worker List:")
        for i, worker in enumerate(WorkerRegistry._worker_list):
            print(f"{i}: {worker.name}, {worker.id}")
        
        # Remove a worker by index
        worker_index = int(input("Enter the index of the worker to remove: "))
        if 0 <= worker_index < len(WorkerRegistry._worker_list):
            removed_worker = WorkerRegistry._worker_list.pop(worker_index)
            print(f"\nRemoved worker: {removed_worker.name}, {removed_worker.id}")
        else:
            print("Invalid index. No worker removed.")
        
        # Display the updated worker list
        print("\nUpdated Worker List:")
        for i, worker in enumerate(WorkerRegistry._worker_list):
            print(f"{i}: {worker.name}, {worker.id}")

class GrossPay:
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate
        self.gross = hours * rate

    def grossPay(self):
        return self.gross

def main():
    print("Welcome to EZ Salary Calculator")
    workers = WorkerRegistry.workerList()  # Use WorkerRegistry's list
    
    print("Choose your action: 'Add' to add a Worker, 'Remove' to remove a worker, other input to calculate")
    while True:
        choice = input("Enter management action: ")
        if choice == "Add":
            HRDepartment.addWorker()
        elif choice == "Remove":
            HRDepartment.removeWorker()
        else:
            print("Continuing to salary calculation...")

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
            break

if __name__ == "__main__":
    main()