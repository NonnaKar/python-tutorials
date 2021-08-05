# Example 1
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."


car1 = Car(mileage=20_000, color="blue")
car2 = Car(mileage=30_000, color="red")

print(car1)
print(car2)

# Example 2
# Class inheritance


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)


x = Student("Mike", "Olsen", 2019)
x.welcome()

# Example 3


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


class VolumeMixin:
    def volume(self):
        return self.area() * self.height


class Cube(VolumeMixin, Square):
    def __init__(self, length):
        super().__init__(length)
        self.height = length

    def face_area(self):
        return super().area()

    def surface_area(self):
        return super().area() * 6


cube = Cube(2)
print(cube.surface_area())
print(cube.volume())

# Example 4


class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Methods .__init__() and .__str__() are called DUNDER METHODS
    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


miles = JackRussellTerrier("Miles", 4)
balto = GoldenRetriever("Balto", 7)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")

print(balto.speak())
print(balto.speak("Grrr"))
print(jim.speak("Woof"))

# print(type(jack))
# print(isinstance(jack, Dachshund))
# print(isinstance(jack, Bulldog))
