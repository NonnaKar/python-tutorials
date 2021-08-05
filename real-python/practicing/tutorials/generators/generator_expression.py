
names_list = ['Adam', 'Anna', 'Barry', 'Brianne', 'Charlie']

# generator expression
uppercase = list((name.upper() for name in names_list))
reverse_uppercase = list((name[::-1] for name in uppercase))
print(reverse_uppercase)
