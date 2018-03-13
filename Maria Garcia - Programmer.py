class Person(object):
    def __init__(self, education, name):
        self. education = education
        self.name = name

    def work(self):
        print("%s goes to work." % self.name)
        print("%s has a %s education." % (self.name, self.education))


class Employee(Person):
    def __init__(self, education, name, uniform):
        super(Employee, self).__init__(education, name)
        self.uniform = uniform

    def reads(self):
        print("%s can read an article." % self.name)
        print("%s wears a %s uniform." % (self.name, self.uniform))
        print("%s has a %s education." % (self.name, self.education))


class Programmer(Employee):
    def __init__(self, computer, uniform, name, education):
        super(Programmer, self).__init__(education, name, uniform)
        self.computer = computer

    def types(self):
        print("%s is typing on a %s." % (self.name, self.computer))
        print("%s wears a %s uniform." % (self.name, self.uniform))
        print("%s has a %s education." % (self.name, self.education))


programmer1 = Programmer('Surface Pro', 'dress', 'Sophia', 'college')
employee1 = Employee('high school', 'Robert', 'shirt and jeans')
person1 = Person('college', 'Charles the 23rd')

print("This is the programmer:")
programmer1.types()
print('')
print("This is the employee:")
employee1.reads()
print('')
print("This is the person:")
person1.work()
