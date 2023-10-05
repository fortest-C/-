import json

with open('data.json', 'r') as dt:
    data = json.load(dt)

for d in data:
    print(d, '-->', data[d])