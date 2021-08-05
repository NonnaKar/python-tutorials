family = {'father': 45, 'mother': 42, 'son_1': 18, 'son_2': 18, 'daughter': 12}

# Geting keys 1
key = list(family.keys())
print(key)

# Geting keys 2
family_member = []

for person in family:
    family_member.append(person)
print(family_member)

# Geting values 1
v = list(family.values())
print(v)

# Geting values 2
ages = []

for person, age in family.items():
    ages.append(age)
print(ages)
