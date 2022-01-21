class FirstHundredGenerator:
    def __init__(self):
        self.number = 0;

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter(self):
        return self


# the above iter method can do the same thing

class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()


print(sum(FirstHundredIterable()))

'''for i in FirstHundredGenerator():
    print(i)'''


class AnotherIterable:
    def __init__(self):
        self.cars = ['fiesta', 'focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


for car in AnotherIterable():
    print(car)

my_num = [x for x in [1, 2, 3, 4, 5]]
my_num_gen = (x for x in [1, 2, 3, 4, 5]) # generator comprehension

print(next(my_num_gen))
