my_dict = {"name": "annie", "age": "70"}
print(my_dict)

#a python dictionary is like a javascript object having key-value pairs.
#dictionaries are optimised for fast look-up and can use immutable types as keys
#used in data management, configuration, and lookups

person = {"name": "Alice", "age": 30}
person["city"] = "New York" #adds a new key-value pair
print(person["name"]) #output: Alice
del person["age"] #removing a key-value pair by just targeting the key
print(person)

#methods also include: get, keys, values, items to access and manipulate dictionary contents
