#python has the module "json" that allows for parsing and generation of JSON data

import json

#convert dictionary to JSON string
person_dict = {"name": "Alice", "age": 30}
person_json =json.dumps(person_dict)
print(person_json)

#parse JSON string to dictionary
parsed_dict = json.loads(person_json)
print(parsed_dict) #Output: {'name': 'Alice', 'age': 30}