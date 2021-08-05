
# * Using if statement

from itertools import cycle
from collections import ChainMap
name = 'Joe'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Joe':
    print('Hello Joe')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

# * Using dictionaries

names = {
    'Fred': 'Hello Fred',
    'Xander': 'Hello Xander',
    'Joe': 'Hello Joe',
    'Arnold': 'Hello Arnold'
}

print(names.get('Joe', "I don't know who you are!"))
print(names.get('Rick', "I don't know who you are!"))

# * Conditional Expressions
age = 12
s = 'minor' if age < 21 else 'adult'

'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'

# * Iterating a dict
# Example 1


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# * Iterating a dict
# Example 2


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

# * Turning Keys Into Values and Vice Versa
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {}
for k, v in a_dict.items():
    new_dict[v] = k

print(new_dict)

# * Filtering Items
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {}
for k, v in a_dict.items():
    if v <= 2:
        new_dict[k] = v

print(new_dict)

# * Doing Some Calculations
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = 0.00
for value in incomes.values():
    total_income += value

print(total_income)

# * Using Comprehensions
objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']
a_dict = {key: value for key, value in zip(categories, objects)}

print(a_dict)

# * Turning Keys Into Values and Vice Versa: Revisited
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {value: key for key, value in a_dict.items()}
print(new_dict)

# * Filtering Items: Revisited
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {k: v for k, v in a_dict.items() if v <= 2}
print(new_dict)

# * Doing Some Calculations: Revisited
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = sum(incomes.values())
# total_income = sum([value for value in incomes.values()])
# total_income = sum([value for value in incomes.values()]) --- generator expression --- save memory
print(total_income)

# * Removing Specific Items
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
non_citric = {k: incomes[k] for k in incomes.keys() - {'oranges'}}
print(non_citric)

# * Sorting a Dictionary
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
sorted_income = {k: incomes[k] for k in sorted(incomes)}
print(sorted_income)

# Python’s map() is defined as map(function, iterable, ...)
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}


def discount(current_price):
    return (current_price[0], round(current_price[1] * 0.95, 2))
    # current_price[0] represents the key and round(current_price[1] * 0.95, 2) represents the new value


new_prices = dict(map(discount, prices.items()))
print(new_prices)

# filter() is defined as filter(function, iterable)
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}


def has_low_price(price):
    return prices[price] < 0.4


low_price = list(filter(has_low_price, prices.keys()))
print(low_price)

# * Using collections.ChainMap

# With ChainMap, you can group multiple dictionaries together to create a single, updateable view.
# Now, suppose you have two (or more) dictionaries, and you need to iterate through them together as one.

fruit_prices = {'apple': 0.40, 'orange': 0.35}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
chained_dict = ChainMap(fruit_prices, vegetable_prices)

for key in chained_dict:
    print(key, '->', chained_dict[key])

# * Using itertools
# Python’s itertools is a module that provides some useful tools to perform iteration tasks.

# * Cyclic Iteration With cycle()
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
times = 3  # Define how many times you need to iterate through prices
total_items = times * len(prices)
for item in cycle(prices.items()):
    if not total_items:
        break
    total_items -= 1
    print(item)

# * Using the Dictionary Unpacking Operator (**)
fruit_prices = {'apple': 0.40, 'orange': 0.35}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
# How to use the unpacking operator **
{**vegetable_prices, **fruit_prices}
# You can use this feature to iterate through multiple dictionaries
for k, v in {**vegetable_prices, **fruit_prices}.items():
    print(k, '->', v)
