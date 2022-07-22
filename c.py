import json

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

with open('config.json', 'r') as c:
    kartik = json.load(c)["kartik"]

print(kartik['kd'])
print(params['local_server'])
