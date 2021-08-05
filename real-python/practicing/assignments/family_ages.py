
## ASSIGNMENT - 2
#PROBLEM:
# Given a dictionary of 'family_ages' as shown below
# get the output of family_ages after 1 year from the present
family_ages = {
    'Mother': 45,
    'Father': 50,
    'Sister': 20,
    'Brother': 18
}

# Variant 1 getting a value 
# ages = []
# for person, age in family_ages.items():
#     ages.append(age)
# for age in range(len(ages)):
#     ages[age] += 1


# Variant 2 geting a value
ages = [] # getting a value of the dictionary
new_ages = [] #getting the updated value of the dictionary
person = [] # getting a key of the dictionary

# Actual code 
# step 1
ages = list(family_ages.values())
new_ages = [age+1 for age in ages] # list comprehension

# step 2
person = list(family_ages.keys())

# step 3
#  we have key person and value new_ages
# use zip() function to add lists of key and value into a dictionary

# new_ages = [46, 51, 21, 19]
# person = ['Mother', 'Father', 'Sister', 'Brother']

new_family_ages = dict(zip(person, new_ages))

# Variant 3 to get the result 

def add_age(a):
    return a + 1
    # new_age = a
    # if a < 20:
    #     new_age = 2 * a
    # elif a >= 50:
    #     new_age = a
    # else:
    #     new_age = a + 10
    # return new_age

# dictionary = { key: value for key, value in dictionary.items()}
new_family_ages = {person:add_age(age) for person, age in family_ages.items()} # dict comprehension

new_family_ages1 = {person.lower():age for person, age in family_ages.items()} # dict comprehension

print(new_family_ages1)
print(new_family_ages)