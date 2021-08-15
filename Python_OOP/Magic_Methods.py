class Employee:
    raise_amount = 1.04
    # dunder init
    def __init__(self, first, last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "." + "@company.com"

        #Employee.num_of_emps += 1

    def __repr__(self):
        return "Employee('{}' , '{}' ,'{}')".format(self.first,self.last,self.pay)


    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


    def fullname(self):
        return (f'The employee name is : {self.first} {self.last}')

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)




emp1 = Employee('Geeta', 'Kumari', 50000)
emp2 = Employee('Saurav', 'Kumar', 70000)

print(len(emp1))


print('test'.__len__()) # len dudner method

print(emp1+emp2)

'''print(emp1)
print(repr(emp1))
print(str(emp1))
print(emp1.__str__())

print(1+2)
print(int.__add__(1,2))
print(str.__add__('a','2'))'''

