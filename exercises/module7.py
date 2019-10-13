class Animal:
    color = 'black'
    legs = 4

    def walk(self):
        print('Animal is walking')

dog = Animal()
dog.color
dog.walk()

Animal.__dict__

dog.__dict__
Animal.color

class Animal:

    def __init__(self,color,legs):
        self.color = color
        self.legs = legs

    def walk(self):
        print('Animal is walking.')

# dog = Animal('white', 4)
# dog.color
# dog.walk()
#
# Animal.__dict__
# dog.__dict__

class Dog(Animal):
    pass

class Dog(Animal):
    def __init__(self,name,legs,color):
        super().__init__(legs,color)
        self.name = name

    def walk(self):
        print('Dog is walking')

    def bark(self):
        print('Dog is barking')

dog = Dog('Lucky', 4, 'Black')
dog.name
dog.walk()
dog.bark()

spider = Animal('black', 8)
spider.walk()
spider.color
spider.legs


class Counter:
    count = 0

    def increment_1(self):
        self.count += 1

    def increment_n(self, n):
        self.count += n

    def reset(self):
        self.count = 0
counter = Counter()
counter.count
counter.increment_1()
counter.count
counter.increment_n(10)
counter.count
counter.reset()
counter.count

class Rectangle:
    color = 'black'

    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def area(self):
        return self.length * self.width

    def __del__(self):
        print('This rectangle is destroyed')

    def print_class_color():
        print(Rectangle.color)

    def print_instance_color(self):
        print(self.color)

rect = Rectangle(4,6, 'white')
rect.area()
del rect
rect.print_instance_color()
Rectangle.print_class_color()
rect.print_class_color()

class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length, 'white')

    def perimeter(self):
        print("Perimeter = {}".format(4*self.length))

sqaure = Square(4)
sqaure.perimeter()
sqaure.area()



class Employee():

	empCount = 0

	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def __del__(self):
		Employee.empCount -= 1

	def disp_empCount():
		print("Employee Count = {}".format(Employee.empCount))

	def disp_empDetails(self):
		print("{} salary is {}".format(self.name, self.salary))

emp1 = Employee('A', 4000)
Employee.empCount
Employee.disp_empCount()
emp1.disp_empDetails()

emp2 = Employee('B', 3000)
Employee.disp_empCount()
Employee.empCount
del emp2
Employee.disp_empCount()
Employee.empCount



class FullTimeStaff(Employee):

	def __init__(self,name,salary,leave):
		super().__init__(name,salary)
		self.leave = leave

	def disp_EmpDetail(self):
		print("{} salary is ${} and leave is {}days".format(self.name,self.salary,self.leave))

class PartTimeStaff(Employee):

	def __init__(self,name,hrrate):
		super().__init__(name,0)
		self.hrrate = hrrate
		Employee.empCount -=  1

	def __del__(self):
		pass

	def disp_EmpDetail(self):
		print("{} hourly rate is ${} per hour".format(self.name,self.hrate))

# Testing
ally = FullTimeStaff("Ally",4000,21)
belinda = FullTimeStaff("Belinda",4000,21)
jane = PartTimeStaff("Jane",200)
steve = PartTimeStaff("Steve",200)
Employee.disp_empCount()
del belinda
del steve
Employee.disp_empCount()


# Polymerism
class Animal():
    def __init__(self,color,legs):
        self.color = color
        self.legs = legs

    def __del__(self):
        print("i am destroyed")

    def talk(self):
        print("talk like an animal")

class Dog(Animal):

	def __init__(self,color,name):
		super().__init__(color,4)
		self.name = name

	def talk(self):
		print("{} woof woof woof".format(self.name))

class Cat(Animal):

	def __init__(self,color,name):
		super().__init__(color,4)
		self.name = name

	def talk(self):
		print("{} meow meow meow".format(self.name))

a1 = Animal('blue', 'amy')
d1 = Dog("white","ally")
c1 = Cat("black","belinda")

def sound(any):
	any.talk()

sound(d1)
sound(c1)
sound(a1)
