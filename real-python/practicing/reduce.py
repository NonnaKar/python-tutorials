from functools import reduce
from operator import add
from math import prod
from itertools import accumulate

# functools.reduce(function, iterable[, initializer])


# * Example 1
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


# * Example 2
def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


my_add(5, 5)
numbers = [0, 1, 2, 3, 4]
reduce(my_add, numbers, 100)


# * Example 3
numbers = [1, 2, 3, 4]
x = reduce(lambda a, b: a + b, numbers)
print(x)


# * Example 4
add(1, 2)
numbers = [1, 2, 3, 4]
x = reduce(add, numbers)
print(x)

# * Example 5 -- the most pythonic way to use build-in func sum()
numbers = [1, 2, 3, 4]
x = sum(numbers)
print(x)


# * Example 6
numbers = [1, 2, 3, 4]
product = 1
for num in numbers:
    product *= num

print(product)


# * Example 7
def my_prod(a, b):
    return a * b


my_prod(1, 2)
numbers = [1, 2, 3, 4]
x = reduce(my_prod, numbers)
print(x)


# * Example 8
numbers = [1, 2, 3, 4]
x = prod(numbers)
print(x)


# * Example 9
# Minimum
def my_min_func(a, b):
    return a if a < b else b


# Maximum
def my_max_func(a, b):
    return a if a > b else b


numbers = [3, 5, 2, 4, 7, 1]
print(reduce(my_min_func, numbers))
print(reduce(my_max_func, numbers))


# * Example 10
numbers = [3, 5, 2, 4, 7, 1]
print(min(numbers))
print(max(numbers))


# * Example 11
numbers = [1, 2, 3, 4]
x = list(accumulate(numbers))
print(x)
y = reduce(add, numbers)
print(y)


# ! Python’s reduce() can have remarkably bad performance because it works by calling functions multiple times.
# !This can make your code slow and inefficient.
# ! Using reduce() can also compromise the readability of your code when you use it with complex user-defined functions or lambda functions.

#  * Use a dedicated function to solve use cases for Python’s reduce() whenever possible. Functions such as sum(), all(), any(), max(), min(), len(), math.prod(), and so on will make your code faster and more readable, maintainable, and Pythonic.

# * Avoid complex user-defined functions when using reduce(). These kinds of functions can make your code difficult to read and understand. You can use an explicit and readable for loop instead.

# * Avoid complex lambda functions when using reduce(). They can also make your code unreadable and confusing.
