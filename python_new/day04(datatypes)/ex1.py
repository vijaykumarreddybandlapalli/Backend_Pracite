# today we have discus data types of second is method  a Dictranary.
#Dictionary :IN python, A dictionary is a collection of key-value pairs, where each key is unique and is associated with a specific value.
# Syntex:Defined using curly braces {}, with each key-value pair separated by a colon : and each pair separated by a comma.
# from selenium.webdriver.common.devtools.v85.dom import get_node_for_location

# Assign values :Use my_dict[key] or my_dict.get(key) to access values by key.
# some main common operates:
# Add/Update: my_dict[key] = value
# Remove: my_dict.pop(key) or del my_dict[key]
# Retrieve Keys: my_dict.keys()
# Retrieve Values: my_dict.values()
# Retrieve Key-Value Pairs: my_dict.items()
Person_info={
    "Common_man":{ "name" : "vijay" , "age" : 56 , "location" : "bangalore"},
    "person_id":{ "name" : "babu" , "age" : 5622 , "location" :"power_build"}
}
print(Person_info.keys())
# dict_keys(['Common_man', 'person_id'])
print(Person_info.values())
# dict_values([{'name': 'vijay', 'age': 56, 'location': 'bangalore'}, {'name': 'babu', 'age': 5622, 'location': 'power_build'}])
# Person_info["Common_man"]="owner"   # Add/Update: my_dict[key] = value
# print(Person_info)

del Person_info["person_id"]["location"] #Remove: my_dict.pop(key) or del my_dict[key]
print(Person_info)
#Update: my_dict[key] = value

# Update age of Common_man
Person_info["Common_man"]["age"] = 57
print(Person_info)  # Should output 57

# {'Common_man': {'name': 'vijay', 'age': 56, 'location': 'bangalore'}, 'person_id': {'name': 'babu', 'age': 5622}}
# {'Common_man': {'name': 'vijay', 'age': 57, 'location': 'bangalore'}, 'person_id': {'name': 'babu', 'age': 5622}}

# {'Common_man': 'owner', 'person_id': {'name': 'babu', 'age': 5622, 'location': 'power_build'}}



print(Person_info.items())
# dict_items([('Common_man', {'name': 'vijay', 'age': 57, 'location': 'bangalore'}), ('person_id', {'name': 'babu', 'age': 5622})])
print(type(Person_info["Common_man"]))
# <class 'dict'>