# Given a dictionary of fruits as:
fruits = {
    'grapes': {'color': 'green', 'taste': 'sour'},
    'mango': {'color': 'yellow', 'taste': 'sweet'}, 
    'cherry': {'color': 'red', 'taste': 'sweet-sour'}, 
    'strawberry': {'color': 'red', 'taste': 'bitter'}, 
    'banana': {'color': 'yellow', 'taste': 'salty'}, 
    'peach': {'color': 'pink', 'taste': 'tangy'},
    'papaya': {'color': 'pink', 'taste': 'spicy'},
}

# convert the fruits to more usable format as shown below:
# Expected Output
# fruits = {
#     'green': ['grapes'],
#     'yellow': ['mango', 'banana'],
#     'pink': ['peach', 'papaya'],
#     'red': ['cherry', 'strawberry']
# }

##################################################################################################
temp_dict = {}
color_dict = list(fruits.values())
color_list = list(set([key['color'] for key in color_dict]))
# print(color_list)
# temp_dict = dict.fromkeys(color_list, []) Caution: same value '[]' applies for all keys and shares same address in the memory

for color in color_list:
    temp_dict[color] = []
# temp_dict = {
#     "green": [],
#     "pink": [],
#     "yellow": [],
#     "red": []
# }

for temp_dict_key, temp_dict_val in temp_dict.items():
    for fruits_key, fruits_value in fruits.items():
        fruits_color = fruits_value['color']
        print(fruits_color)
        if temp_dict_key == fruits_color:
            temp_dict_val.append(fruits_key)

print(temp_dict)
# fruits = {
#     'grapes': {'color': 'green', 'taste': 'sour'},
#     'mango': {'color': 'yellow', 'taste': 'sweet'}, 
#     'cherry': {'color': 'red', 'taste': 'sweet-sour'}, 
#     'strawberry': {'color': 'red', 'taste': 'bitter'}, 
#     'banana': {'color': 'yellow', 'taste': 'salty'}, 
#     'peach': {'color': 'pink', 'taste': 'tangy'},
#     'papaya': {'color': 'pink', 'taste': 'spicy'},
# }
