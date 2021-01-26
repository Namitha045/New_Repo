import json

def sort_json(package):
    return package['analytics']['30d']

with open('package_info.json','r') as f:
    r = json.load(f)
r.sort(key=sort_json, reverse=True)
data_str = json.dumps(r, indent=2)
print(data_str)


