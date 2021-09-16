data = ["a", "b", True, (False, 1), {"1": 2}, [1, 2], {"2": "two"}, {2, "3"}, "c", 23, 0]
# desirable outcome: {"bool": 1, "int": 2, "list": 1, "tuple": 1, "str": 3}
types = ["int", "str", "bool", "list", "tuple", "dict", "set"]
{}.fromkeys(types, 0)
#{'int': 0, 'str': 0, 'bool': 0, 'list': 0, 'tuple': 0, 'dict': 0, 'set': 0}
total = {}.fromkeys(types, 0)
print(total)                    # {'int': 0, 'str': 0, 'bool': 0, 'list': 0, 'tuple': 0, 'dict': 0, 'set': 0}
for i in range(len(data)):
    if type(data[i]) == int: total["int"] += 1
    elif type(data[i]) == str: total["str"] += 1
    elif type(data[i]) == bool: total["bool"] += 1
    elif type(data[i]) == list: total["list"] += 1
    elif type(data[i]) == tuple: total["tuple"] += 1
    elif type(data[i]) == dict: total["dict"] += 1
    elif type(data[i]) == set: total["set"] += 1

print(total)    # {'int': 2, 'str': 3, 'bool': 1, 'list': 1, 'tuple': 1, 'dict': 2, 'set': 1}
