import json
dict1 ={"name": "Lisa","designation": "programmer","age": "34","salary": "54000" }
y=json.dumps(dict1,indent=4)
print(y)
print(type(y))