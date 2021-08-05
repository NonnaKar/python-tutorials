from class_ninja import Planet

naboo = Planet('Naboo', 200000, 5.5, 'Naboo System')
print(f'Name is: {naboo.name}')
print(f'Radius is: {naboo.radius}')
print(f'Gravity is: {naboo.gravity}')
print(naboo.orbit())
