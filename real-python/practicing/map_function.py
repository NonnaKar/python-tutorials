# Example 1uation
import re
from itertools import starmap
import math


def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)
print(list(squared))

# Example 2
str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]

int_nums = map(int, str_nums)
int_list = list(int_nums)
print(int_list)

# Example 3
numbers = [-2, -1, 0, 1, 2]

abs_values = list(map(abs, numbers))
float_values = list(map(float, numbers))
print(abs_values)
print(float_values)

# Example 4
words = ["Welcome", "to", "Real", "Python"]

len_words = list(map(len, words))
print(len_words)

# Example 5
numbers = [1, 2, 3, 4, 5]

squared = map(lambda num: num ** 2, numbers)
print(list(squared))

# Example 6
first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]

print(list(map(pow, first_it, second_it)))

# Example 7
minus_result = list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5]))
print(minus_result)

plus_result = list(map(lambda x, y, z: x + y + z, [2, 4], [1, 3], [7, 8]))
print(plus_result)

# Example 8
string_it = ["processing", "strings", "with", "map"]

capitalize_str = list(map(str.capitalize, string_it))
print(capitalize_str)

# Example 9


def remove_punctuation(word):
    return re.sub(r'[!?.:;"()-]', "", word)


print(remove_punctuation("...Python!"))

text = """Some people, when confronted with a problem, think
... "I know, I'll use regular expressions."
... Now they have two problems. Jamie Zawinski"""

words = text.split()
print(words)
without_punct = list(map(remove_punctuation, words))

# Example 10
# Implementing a Caesar Cipher Algorithm


def rotate_chr(c):
    rot_by = 3
    c = c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if c not in alphabet:
        return c
    rotated_pos = ord(c) + rot_by
    if rotated_pos <= ord(alphabet[-1]):
        return chr(rotated_pos)
    return chr(rotated_pos - len(alphabet))


secret_message = "".join(map(rotate_chr, "My secret message goes here."))
print(secret_message)

# Example 11

numbers = [1, 2, 3, 4, 5]

factorial_list = list(map(math.factorial, numbers))
print(factorial_list)

# Example 12


def to_fahrenheit(c):
    return 9 / 5 * c + 32


def to_celsius(f):
    return (f - 32) * 5 / 9


c_temp = [100, 40, 80]
fahrenheit = list(map(to_fahrenheit, c_temp))
print(fahrenheit)

f_temp = [212, 104, 176]
celsius = list(map(to_celsius, f_temp))

# Example 13


def is_positive(num):
    return num >= 0


def sanitized_sqrt(numbers):
    cleaned_iter = map(math.sqrt, filter(is_positive, numbers))
    return list(cleaned_iter)


res = sanitized_sqrt([25, 9, 81, -16, 0])
print(res)

# Example 14

print(list(starmap(pow, [(2, 7), (4, 3)])))

# Using List Comprehensions
# Example 15
# Generating a list with map
list(map(function, iterable))

# Generating a list with a list comprehension
[function(x) for x in iterable]

# Example 16
# Transformation function


def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5, 6]

# Using map()
x = list(map(square, numbers))
print(x)

# Using a list comprehension
y = [square(x) for x in numbers]
print(y)

# Using a generator expression
gen_exp = (square(x) for x in numbers)
print(list(gen_exp))
