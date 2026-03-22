# Classes
# class Point:
#     def move(self):
#         print("move")

#     def draw(self):
#         print("draw")

# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)

# point1.draw()

# point2 = Point()
# point2.x = 1
# print(point2.x)

# Constructors - __init__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point = Point(10, 20)
point.x = 11
# print(point.x, point.y)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("John Smith")
# print(john.name)
# john.talk()

bob = Person("Bob Smith")
# bob.talk()

# Inheritance
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def meow(self):
        print("meow")

dog = Dog()
dog.walk()
dog.bark

cat = Cat()
cat.walk()
cat.meow()