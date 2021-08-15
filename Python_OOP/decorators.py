class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last
        #self.email = first + last + "." + "@company.com"

        #Employee.num_of_emps += 1

    @property
    def fullname(self):
        return (f'The employee name is : {self.first} {self.last}')

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @fullname.setter
    def fullname(self,name):
        first,last = name.split (' ')
        self.first = first
        self.last = last


    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp1 = Employee('Geeta', 'Kumari')
emp2 = Employee('Saurav', 'Kumar')


emp1.fullname ='Meeta kumari'
#emp1.first ='git'

print(emp1.first)
#print(emp1.fullname())
print(emp1.fullname)
print(emp1.email) # no need to use emial() with () with the use of @property

del emp1.fullname

print(emp1.first)
#print(emp1.fullname())
print(emp1.fullname)
print(emp1.email) #