
'''
Firstly, a regular method is the type of method that we are used to seeing since the start of OOP tutorials. It is accessible through both the class and the instance, which means that we can call for the method in both
Employee.method()
and
emp_1.method()
they automatically have the instance as the first positional argument, as self.
Secondly, class methods are the type of method used when a method is not really about an instance of a class, but the class itself. To create a class method, just add '@classmethod' a line before creating the class method. The class is automatically the first argument to be passed in, and is represented as 'cls' instead of 'class'. This is because 'class' is already assigned to be something else in Python. There are 2 ways of using the class method as far as Corey has shown.
First is modifying the class variable. Corey modified the 'raise_amount' class variable using a class method. Just remember that to access a class variable, we have to write 'cls.' before specifying the actual name. For example, as 'cls.raise_amount' as in the video.
Second is making an alternative constructor. Sometimes people have information of their specific instances of the class available in a specific format. Corey shows an example of this where first and last names and pay are separated by a hyphen. Corey creates a class method that returns the class with the specific values passed in that are obtained by using split() method to the string passed in. User of the script can now automatically create a new instance without having to parse the string at '-'.
Static methods are different from regular methods an class methods in that it doesn't have a class or instance that is automatically passed in as a firs positional argument. They can be created by adding '@staticmethod' a line before defining the method. These are methods that have a logical connection to the Class, but does not need a class or instance as an argument. Corey says that it is better to make sure we create a static method rather then class or regular method when we are sure that we don't make use of the class or instance within the method.
'''
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

    @classmethod
    def set_raise_amt(cls,amount): # cls is used for class variable
        cls.raise_amount = amount

    # another way of writing constructor of our own, cls is class
    @classmethod
    def from_string(cls, emp_str):
        first, last , pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

emp1 = Employee('Geeta', 'Kumari', 'geeta1')
emp2 = Employee('Saurav', 'Kumar', 'saurav1')



emp1.set_raise_amt(1.09)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp_str1 = 'geeta-kumari-50000'
new_emp1 = Employee.from_string(emp_str1)

print(emp1.first)
print(new_emp1.first)

import datetime

my_date = datetime.date(2016,7,10)
print(Employee.is_workday(my_date))