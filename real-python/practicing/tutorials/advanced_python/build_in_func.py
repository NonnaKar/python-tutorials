import itertools


# * demonstrate built-in utility functions

def main():
    # use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]

    # TODO: any will return true if any of the sequence values are true
    print(any(list1))

    # TODO: all will return true only if all values are true
    print(all(list1))

    # TODO: min and max will return minimum and maximum values in a sequence
    print("min: ", min(list1))
    print("max: ", max(list1))

    # TODO: Use sum() to sum up all of the values in a sequence
    print("sum: ", sum(list1))


if __name__ == "__main__":
    main()


# * use iterator functions like enumerate, zip, iter, next

def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO: use iter to create an iterator over a collection
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))

    # TODO: iterate using a function and a sentinel
    with open("testfile.txt", "r") as fp:
        for line in iter(fp.readline, ''):
            print(line)

    # TODO: use regular interation over the days
    for m in range(len(days)):
        print(m+1, days[m])

    # TODO: using enumerate reduces code and provides a counter
    for i, m in enumerate(days, start=1):
        print(i, m)

    # TODO: use zip to combine sequences
    for i, m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], "=", m[1], "in French")


if __name__ == "__main__":
    main()


# * use transform functions like sorted, filter, map

def filterFunc(x):
    if x % 2 == 0:
        return True
    return False


def filterFunc2(x):
    if x.isupper():
        return False
    return True


def squareFunc(x):
    return x ** 2


def toGrade(x):
    if (x >= 90):
        return "A"
    elif (x >= 80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    return "F"


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: use filter to remove items from a list
    even = list(filter(filterFunc, nums))
    print(even)

    # TODO: use filter on non-numeric sequence
    lowers = list(filter(filterFunc2, chars))
    print(lowers)

    # TODO: use map to create a new sequence of values
    squares = list(map(squareFunc, nums))
    print(squares)

    # TODO: use sorted and map to change numbers to grades
    grades = sorted(grades)
    letters = list(map(toGrade, grades))
    print(letters)


if __name__ == "__main__":
    main()


# * advanced iteration functions in the itertools package

def testFunction(x):
    return x < 40


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    # TODO: use count to create a simple counter
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # TODO: accumulate creates an iterator that accumulates values
    vals = [10, 20, 30, 40, 50, 40, 30]
    acc = itertools.accumulate(vals, max)
    print(list(acc))

    # TODO: use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(list(x))

    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))


if __name__ == "__main__":
    main()
