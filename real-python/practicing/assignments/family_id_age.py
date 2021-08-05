## ASSIGNMENT - 3
## Date: Feb 07 2021

family_ages = {
    'Mother': 45,
    'Father': 50,
    'Sister': 20,
    'Brother': 18,
    'Nephew': 54
}

family_ids = {
    'Mother': '#001', 
    'Father': '#002',
    'Brother': '#111',
    'Sister': '#112',
    'Niece': '#456'
}

#*********************** Problem ******************************
# Given two dictionaries 'family_ages' & 'family_ids' 
# as shown above. Get the combined data list of 
# age & id for each person in family as shown in expected output
# if relation's id in not known -default it to '###'
#***************************************************************

#*********************** Exprected Output **********************
# family_details = [
#     {'relation': 'Mother', 'id': '#001'},
#     {'relation': 'Father', 'id': '#002'},
#     {'relation': 'Brother', 'id': '#111'},
#     {'relation': 'Sister', 'id': '#112'}
#     {'relation': 'Niece', 'id': '#113'},
#     {'relation': 'Nephew', 'id': '###'}
# ]
#***************************************************************

#******************* Start your code here **********************

family_details = []

family_ages_keys = list(family_ages.keys()) #['Mother', 'Father', 'Brother', 'Sister]
family_ids_keys = list(family_ids.keys()) #['Mother', 'Father', 'Brother', 'Sister, 'Niece']

all_relations_list = family_ages_keys + family_ids_keys 
#['Mother', 'Father', 'Brother', 'Sister, 'Niece', 'Mother', 'Father', 'Brother', 'Sister]

all_relations_list = list(set(all_relations_list))
#['Mother', 'Father', 'Brother', 'Sister, 'Niece', 'Nephew']
try:
    # for key, value in family_ids.items():
    #     temp_dict = {}
    #     temp_dict['relation'] = key
    #     temp_dict['id'] = value
    #     family_details.append(temp_dict)
    for r in all_relations_list:
        temp_dict = {}
        temp_dict['relation'] = r
        if r in family_ids.keys():
            temp_dict['id'] = family_ids[r]
        else:
            temp_dict['id'] = '###'
        family_details.append(temp_dict)
except:
    raise
print(family_details)



#******************* End your code here **********************
