import json
table = []
with open("data.json", "r") as data_file:
    table.append(json.load(data_file))

print(table[0]["pornoski"]["email"])
