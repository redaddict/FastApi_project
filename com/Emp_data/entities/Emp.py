class Emp:

    def __init__(self, Id, Emp_name, Emp_salary):
        self.Id = Id
        self.Emp_name = Emp_name
        self.Emp_salary = Emp_salary

    def getId(self):
        return self.Id

    def setId(self, Id):
        self.Id = Id

    def getName(self):
        return self.Emp_name

    def setName(self, Emp_name):
        self.Emp_name = Emp_name

    def getSalary(self):
        return self.Emp_salary

    def setSalary(self, Emp_salary):
        self.Emp_salary = Emp_salary

    def to_string(self):
        return f" Employee(Id = {self.Id}, Emp_name = {self.Emp_name}, Emp_salary = {self.Emp_salary})"
