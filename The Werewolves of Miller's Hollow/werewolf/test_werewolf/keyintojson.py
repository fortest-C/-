import json

with open('data.json', 'r', encoding="utf8") as jdata:
    data= json.load(jdata)

data['msg9'] = "[玩家, 可否施法]"


with open('data.json', 'w') as jdata:
    json.dump(data, jdata, indent=4)