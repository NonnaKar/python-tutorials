##################################################################################################
# Given a sentence as:
sentence = 'Life is 10 percent what happens and 90 percent how you react to it'    
# Reverse the given sentence
words = sentence.split()
words = list(reversed(words))
reverse_sentence = " ".join(words)
print(reverse_sentence)
# Expected Output
reverse_sentence = 'it to react you how percent 90 and happens what percent 10 is Life'

##################################################################################################
# From the given input list find a number which is closest to 500
numbers_input = input("Enter numbers: ")
num = list(map(int, numbers_input.split()))
print("Numbers: ", num)

minus_num = 500
dist_minus_num = [x-minus_num for x in num]
abs_val_list = [abs(n) for n in dist_minus_num]
min_abs_val_list = min(abs_val_list)
index_of_min_abs_val_list = abs_val_list.index(min_abs_val_list)
closest_to_minus_num = num[index_of_min_abs_val_list]
print(closest_to_minus_num)

##################################################################################################
# Given a List of countries as:
countries = ['USA', 'Belize', 'Seychelles', 'Oman']
countries = countries[::-1]
print(countries)
# reverse the countries list as:
# Expected Output
countries = ['Oman', 'Seychelles', 'Belize', 'USA']

##################################################################################################
# Given a random sentence as:
random_sentence = input("Write a sentence: ")
#Interchange the genders in the above given sentence
# Expected Output
# interchanged_sentence = "she wasn't bitter that he had moved on but from the radish."

##################################################################################################
# Given a dictionary of fruits as:
fruits = {
    'grapes': {'color': 'green'}, 
    'mango': {'color': 'yellow'}, 
    'cherry': {'color': 'red'}, 
    'strawberry': {'color': 'red'}, 
    'banana': {'color': 'yellow'}, 
    'peach': {'color': 'pink'},
    'papaya': {'color': 'pink'},
}

# convert the fruits to more usable format as shown below:
# Expected Output
fruits = {
    'green': ['grapes'],
    'yellow': ['mango', 'banana'],
    'pink': ['peach', 'papaya'],
    'red': ['cherry', 'strawberry']
}

##################################################################################################
