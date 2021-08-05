
# * Sorting Numbers
# Example 1
from collections import namedtuple
numbers = [6, 9, 3, 1]
s = sorted(numbers)
print(s)

# Example 2
num_tuple = (6, 9, 3, 1)
num_set = {6, 9, 3, 1}
num_tuple_sorted = sorted(num_tuple)
num_set_sorted = sorted(num_set)
print(num_tuple_sorted)
print(num_set_sorted)

print(tuple(num_tuple_sorted))
print(set(num_set_sorted))

# * Sorting Strings
# Example 1
string_number_value = '34521'
string_value = 'I like to sort'
sorted_string_number = sorted(string_number_value)
sorted_string = sorted(string_value)
print(sorted_string_number)
print(sorted_string)

# * sorted() With a key Argument
# Example 1
words = ['banana', 'pie', 'Washington', 'book']
s = sorted(words, key=len)
print(s)

# Example 2
names_with_case = ['harry', 'Suzy', 'al', 'Mark']
s = sorted(names_with_case)
k = sorted(names_with_case, key=str.lower)
print(s)
print(k)

# Example 3

StudentFinal = namedtuple('StudentFinal', 'name grade')
bill = StudentFinal('Bill', 90)
patty = StudentFinal('Patty', 94)
bart = StudentFinal('Bart', 89)
students = [bill, patty, bart]
x = sorted(students, key=lambda x: getattr(x, 'grade'), reverse=True)
print(x)

# * Using sort()
# Example 1
phrases = ['when in rome', 'what goes around comes around',
           'all is fair in love and war']
phrases.sort(key=lambda x: x.split()[2][1], reverse=True)
print(phrases)

# * When to Use sorted() and When to Use .sort()
# Example 1

Runner = namedtuple('Runner', 'bibnumber duration')
runners = []
runners.append(Runner('2528567', 1500))
runners.append(Runner('7575234', 1420))
runners.append(Runner('2666234', 1600))
runners.append(Runner('2425234', 1490))
runners.append(Runner('1235234', 1620))
runners.append(Runner('2526674', 1906))

runners.sort(key=lambda x: getattr(x, 'duration'))
top_five_runners = runners[:5]
print(top_five_runners)

runners_by_duration = sorted(runners, key=lambda x: getattr(x, 'duration'))
top_five_runners = runners_by_duration[:5]
print(top_five_runners)
