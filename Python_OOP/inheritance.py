'''1. What is inheritence?
It is a method that allows us to create a new class that shares the same attributes and method with the original function, and add some extra functionality to the new class. It also does not disturb the original class.


2. How to make a class inherit from another class?
class Developer(Employee):


3. Structure of classes and subclasses.
When we input a function to a subclass, python follows the 'method resolution order', which is the chain of classes that it goes through to find what the method is. All classes have the built-in group of methods and attributes as their primary order.


4. How to initiate the subclass so that it can handle more information than its original class can?
There are 2 ways.
first, using the super method as follows and pass in the arguments in interest.
super.__init__()


Second, call the parent's init method explicitly and pass in the arguments in interest.
Employee.init(self, first, last, )


5. Useful tools when exploring the inheritance system.
.isinstance(instance, class)
This method returns the boolean value of whether an instance belongs to a calss
.issubclass(subclass, class)
This method returns the boolean value of whether a class has inherited from the second class.

6. Example of class inheritance
Whisky library

++ when setting a default value for an ungiven argument, avoid using an empty mutable data type'''


class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "." + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return (f'The employee name is : {self.first} {self.last}')

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees =[]
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees :
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())


# print(help(Developer))

dev1 = Developer('Geeta', 'Kumari', 50000,'python')
dev2 = Developer('Saurav', 'Kumar', 70000,'java')

# print(dev1.first)

'''print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)'''

#print(dev1.email)
#print(dev1.prog_lang)

mgr1 = Manager('git','sunita',90000,[dev1])
print(mgr1.email)

#mgr1.print_emps()

mgr1.add_emp(dev2)
#mgr1.remove_emp(dev1)

mgr1.print_emps()

print(isinstance(mgr1,Manager))
print(isinstance(mgr1,Employee)) # as manager inherits from employee
print(isinstance(mgr1,Developer))

print(issubclass(Manager,Employee))
print(issubclass(Developer,Employee))
print(issubclass(Manager,Developer))