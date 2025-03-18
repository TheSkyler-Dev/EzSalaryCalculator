#python version of ezsalcalc :p this is a minimal viuable product
class Workers: #class for workers
    def __init__(self, name, id): # constructor
        self.name = name
        self.id = id
    
    @staticmethod
    def workerList(): #list of existing workers
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
    print("Welcome toi EZ Salary Calculator")
    print("Please enter the following information:")
    name = input("Enter the worker's name: ")
    id = int(input("Enter the worker's ID: "))
    
    # Check if the worker exists in the list
    workers = Workers.workerList()
    worker = next((w for w in workers if w.name == name and w.id == id), None)
    
    if worker is None:
        print("Worker not found.")
        return
    
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly rate: "))
    gross = GrossPay(hours, rate)
    result = f"Worker's name: {worker.name}\nWorker's ID: {worker.id}\nGross pay: {gross.gross}"
    print(result)

if __name__ == "__main__":
    main()