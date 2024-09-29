import json
print("######################################## Parse JSON - Convert from JSON to Python ########################################")
#If you have a JSON string, you can parse it by using the json.loads() method.

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
print(f"string to python {json.loads(x)}")

print("########################################Convert from Python to JSON###################################")
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
print(f"python to string {json.dumps(x)}")