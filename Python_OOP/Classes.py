class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = first + last + "." + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return (f'The employee name is : {self.first} {self.last}')

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)
emp1 = Employee('Geeta', 'Kumari', 'geeta1')
emp2 = Employee('Saurav', 'Kumar', 'saurav1')

print(Employee.num_of_emps)
print(emp1.email)
print(emp2.email)
print(Employee.fullname(emp1))
print(emp1.fullname())  # no need to explitly mention the instance variable . 'self' will take care of that

Employee.raise_amount = 1.5
emp1.raise_amount = 1.6

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print(emp1.__dict__)  # to see what values it can get from class
print(Employee.__dict__)
