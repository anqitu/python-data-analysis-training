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



class Account():

    acc_count = 0

    def __init__(self, number, balance):
        self.number = number
        self.balance = balance
        Account.acc_count += 1

    def __del__(self):
        Account.acc_count -= 1

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def disp_total_accounts():
        print("Total accounts: {}".format(Account.acc_count))

    def disp_acc_details(self):
        print("Account Number: {}\nBalance: {}".format(self.number, self.balance))

acc1 = Account('001', 4000)
Account.acc_count
Account.disp_total_accounts()
acc1.disp_acc_details()

acc2 = Account('002', 4000)
Account.disp_total_accounts()
del acc1
Account.disp_total_accounts()

class SavingsAccount(Account):

	def __init__(self, number, balance, interest):
		super().__init__(number, balance)
		self.interest = interest

	def disp_acc_details(self):
		super().disp_acc_details()
        print("Interest: {}".format(self.interest))

    def withdraw(self):
        pass

class CheckingAccount(Account):

    TRANSACTION_FEE = 0.5

	def withdraw(self, amount):
        super().withdraw(amount)
        self.balance -= CheckingAccount.TRANSACTION_FEE

    def deposit(self, amount):
        super().deposit(amount)
        self.balance -= CheckingAccount.TRANSACTION_FEE

class TemporaryAccount(Account):

    def __init__(self, number, balance):
		super().__init__(number, balance)
		Account.acc_count -= 1

    def __del__(self):
        pass

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
