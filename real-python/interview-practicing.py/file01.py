# How to Stand Out in a Python Coding Interview

# * 1 - Iterate With enumerate() Instead of range()
# Example 1
import itertools
import string
from collections import Counter
from collections import defaultdict
import random
numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers):
    if num % 3 == 0 and num % 5 == 0:
        numbers[i] = 'fizzbuzz'
    elif num % 3 == 0:
        numbers[i] = 'fizz'
    elif num % 5 == 0:
        numbers[i] = 'buzz'

print(numbers)

# Example 2
numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers, start=1):
    print(i, num)

# * 2 - Use List Comprehensions Instead of map() and filter()
# Example 1
numbers = [4, 2, 1, 6, 9, 7]


def square(x):
    return x*x


sq_num = [square(x) for x in numbers]
print(sq_num)

# Example 2
numbers = [4, 2, 1, 6, 9, 7]


def is_odd(x):
    return bool(x % 2)


odd_num = [x for x in numbers if is_odd(x)]
print(odd_num)

# * 3 - Debug With breakpoint() Instead of print()
# breakpoint()

# * 4 - Format strings With f-Strings
# Example 1


def get_name_decades(name, age):
    return f"My name is {name} and I'm {age /10:.5f} decades old"


print(get_name_decades("Nonna", 23))

# ! The one risk to be aware of is that if you’re outputting user-generated values,
# ! then that can introduce security risks, in which case Template Strings may be a safer option.

# * 5 - Sort Complex Lists With sorted()
# Example 1
animals = [
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5},
]
sort_by_age = sorted(animals, key=lambda animal: animal['age'])
print(sort_by_age)

# Example 2
x = sorted([3, 81, 1, 7, 23, 9, 11])
print(x)

y = sorted(['cat', 'dog', 'cheetah', 'rhino', 'bear'], reverse=True)
print(y)

# * Leverage Data Structures Effectively
# * 6 - Store Unique Values With Sets
# Example 1
all_words = "all words in the world".split()


def get_random_words():
    return random.choice(all_words)

# Good Approach


def get_unique_words():
    words = set()
    for _ in range(1000):
        words.add(get_random_words())
    return words


print(get_unique_words())

# * 7 - Save Memory With Generators
# Example 1
# Swapping out the brackets changes your list comprehension into a generator expression.
# instead of this:
y = sum([i * i for i in range(1, 1001)])
print(y)
# do this to save memory :
x = sum((i * i for i in range(1, 1001)))
print(x)

# * 8 - Define Default Values in Dictionaries With .get() and .setdefault()
# Example 1
cowboy = {'age': 32, 'horse': 'mustang', 'hat_size': 'large'}
name = cowboy.get('name', 'The Man with No Name')
print(name)

# Example 2
cowboy = {'age': 32, 'horse': 'mustang', 'hat_size': 'large'}
name = cowboy.setdefault('name', 'The Man with No Name')

# * 9 - Take Advantage of Python’s Standard Library
# Handle Missing Dictionary Keys With collections.defaultdict()
# Example 1

# Instead of this:
# student_grades = {}
# grades = [
#     ('elliot', 91),
#     ('neelam', 98),
#     ('bianca', 81),
#     ('elliot', 88),
# ]
# for name, grade in grades:
#     if name not in student_grades:
#         student_grades[name] = []
#     student_grades[name].append(grade)
# print(student_grades)

# Do this:

student_grades = defaultdict(list)
grades = [
    ('elliot', 91),
    ('neelam', 98),
    ('bianca', 81),
    ('elliot', 88),
]
for name, grade in grades:
    student_grades[name].append(grade)
print(student_grades)

# * 10 - Count Hashable Objects With collections.Counter
# Example 1

words = "if there was there was but if there was not there was not".split()
counts = Counter(words)
print(counts)
common_words = counts.most_common(2)
print(common_words)

# * 11 - Access Common String Groups With string Constants
# Example 1


def is_upper(word):
    for letter in word:
        if letter not in string.ascii_uppercase:
            return False
    return True


print(is_upper('Thanks Geir'))
print(is_upper('LOL'))

# * All string constants are just strings of frequently referenced string values. They include the following:
# string.ascii_letters
# string.ascii_uppercase
# string.ascii_lowercase
# string.digits
# string.hexdigits
# string.octdigits
# string.punctuation
# string.printable
# string.whitespace
# These are easier to use and, even more importantly, easier to read.

# * 12 - Generate Permutations and Combinations With itertools
# Example 1

friends = ['Monique', 'Ashish', 'Devon', 'Bernie']
pairs = list(itertools.permutations(friends, r=2))
print(pairs)

comb_pairs = list(itertools.combinations(friends, r=2))
print(comb_pairs)
