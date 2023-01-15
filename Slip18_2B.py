# Slip18_2B
class Person:
    def __init__(self, name : str, address : str):
        self.name = name
        self.address = address
    
class Employee(Person):
    def __init__(self, name: str, address: str, salary : int):
        super().__init__(name, address)
        self.salary = salary
    
    def _display(self):
        print("Name : ",self.name)
        print("Address : ",self.address)
        print("Salary : ",self.salary)


def main():
    N = int(input("Enter number of Employees: "))
    Employees = list()
    for _ in range(N):
        Employees.append(Employee(name=input("Enter Employee's Name: "),address=input("Enter Employee's Address: "),salary=int(input("Enter Employee's Salary: "))))

    for EmployeeDude in Employees:
        EmployeeDude._display()

if __name__=="__main__":
    main()