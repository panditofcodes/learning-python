import json

data = {"key1" : "value1", "key2" : "value2"}
print(type(data))

json_data = json.dumps(data)

print(type(json_data))
print(json_data)