
# * define enumerations using the Enum base class

from enum import Enum, unique, auto


@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()


def main():
    pass
    # TODO: enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    # TODO: enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # TODO: print the auto-generated value
    print(Fruit.PEAR.value)

    # TODO: enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(myFruits[Fruit.BANANA])


if __name__ == "__main__":
    main()


# * customize string representations of objects


class Person():
    def __init__(self):
        self.fname = "Nonna"
        self.lname = "Lisova"
        self.age = 23

    # TODO: use __repr__ to create a string useful for debugging
    def __repr__(self):
        return f"<Person Class - fname:{self.fname}, lname:{self.lname}, age:{self.age}"

    # TODO: use str for a more human-readable string
    def __str__(self):
        return f"Person ({self.fname} {self.lname} {self.age})"

    def __bytes__(self):
        val = f"Person:{self.fname}:{self.lname}:{self.age}"
        return bytes(val.encode('utf-8'))


def main():
    # create a new Person object
    cls1 = Person()

    # use different Python functions to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    print(f"Formatted: {cls1}")
    print(bytes(cls1))


if __name__ == "__main__":
    main()


# * customize string representations of objects


class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # TODO: use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return(self.red, self.green, self.blue)
        elif attr == "hexcolor":
            return "#{self.red:02x}{self.green:02x}{self.blue:02x}"
        else:
            raise AttributeError

    # TODO: use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    # TODO: use dir to list the available properties
    def __dir__(self):
        return("red", "green", "blue", "rgbcolor", "hexcolor")


def main():
    # create an instance of myColor
    cls1 = myColor()
    # TODO: print the value of a computed attribute
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    # TODO: set the value of a computed attribute
    cls1.rgbcolor = (125, 200, 86)
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    # TODO: access a regular attribute
    print(cls1.red)

    # TODO: list the available attributes
    print(dir(cls1))


if __name__ == "__main__":
    main()


# * give objects number-like behavior


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point x:{0},y:{1}>".format(self.x, self.y)

    # TODO: implement addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # TODO: implement subtraction
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # TODO: implement in-place addition
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self


def main():
    # Declare some points
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1, p2)

    # TODO: Add two points
    p3 = p1 + p2
    print(p3)

    # TODO: subtract two points
    p4 = p2-p1
    print(p4)

    # TODO: Perform in-place addition
    p1 += p2
    print(p1)

    p1 -= p2
    print(p1)


if __name__ == "__main__":
    main()


# * Use special methods to compare objects to each other


class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService

    # TODO: implement comparison functions by emp level
    def __ge__(self, other):
        if (self.level == other.level):
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if (self.level == other.level):
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if (self.level == other.level):
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other):
        if (self.level == other.level):
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __eq__(self, other):
        pass


def main():
    # define some employees
    dept = []
    dept.append(Employee("Tim", "Sims", 5, 9))
    dept.append(Employee("John", "Doe", 4, 12))
    dept.append(Employee("Jane", "Smith", 6, 6))
    dept.append(Employee("Rebecca", "Robinson", 5, 13))
    dept.append(Employee("Tyler", "Durden", 5, 12))

    # TODO: Who's more senior?
    print(dept[0] > dept[2])
    print(dept[4] < dept[3])

    # TODO: sort the items
    emps = sorted(dept)
    for emp in emps:
        print(emp.lname)


if __name__ == "__main__":
    main()
