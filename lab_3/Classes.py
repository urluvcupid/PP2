"""
#1
class MyClass:
    x = 5

#2
class MyClass:
    x = 5
p1 = MyClass()

#3
class MyClass:
    x = 5
p1 = MyClass()

print(p1.x)    #5

#4
class Person:
  def __init__ (self, name, age):
    self.name = name
    self.age = age
"""
# Ex. from github itself

#1
class mineclass:
    def __init__(self):
        self.string = ""
    def getstring(self):
        self.string = input("Write a string: ")
    def printstring(self):
        
        print(self.string.upper())
el = mineclass()
el.getstring()
el.printstring()

#2
class Shape:
  def area(self):
    return 0
class Square(Shape):
  def __init__(self, length):
    super().__init__()
    self.length = length
  def area(self):
    return self.length * self.length
square = Square(5)
print(f"The area of the square is: {square.area()}")


#3
class Rectangle(Shape):
  def __init__(self, length, width):
    super().__init__()
    self.length = length
    self.width = width
  def area(self):
    return self.length * self.width
rect = Rectangle(4, 5)
print(f"The area of the rectangle is: {rect.area()}")


#4
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def move(self, x, y):
    self.x += x
    self.y += y
  def show(self):
    print(f"The coordinates are: {self.x} and {self.y}")
  def dist(self, b):
    res = ((self.x - b.x)**2 + (self.y - b.y)**2)**0.5
    print(f'distance between 2 points is: {res}')
p1 = Point(4, 5)
p2 = Point(1, 3)
p1.show()
p2.move(2, 3)
p2.show()
p1.dist(p2)

#5
class Account:
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance
  def info(self):
    print(self.owner)
    print(self.balance)
  def deposit(self, amount):
    self.balance += amount
  def withdraw(self, amount):
    if self.balance - amount < 0:
      print('no enough money to withdraw')
    else:
      self.balance -= amount
Franklin = Account('Franklin', 40000)
Franklin.info()
Franklin.withdraw(25000)
Franklin.deposit(3000)
Franklin.withdraw(25000)
Franklin.info()


#6
def IsPrime(num):
  if num <= 1:
        return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_num = list(filter(lambda x : IsPrime(x), numbers))
print(*prime_num)
