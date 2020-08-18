import requests
import json


# Scan input file
# Print each variant in a line
# Make PUT call to load line into Elastic Search
d = { "index" : { "_index": "variants", "_type" : "_doc", "_id" : "1" } }

with open('dceoy-output.json','r') as f:
    lines = f.readlines()

with open('variants.json','w') as f:
    for idx, line in enumerate(lines): 
        d["index"].update(_id=json.dumps(idx))
        f.write(json.dumps(d))
        f.write("\n")
        f.write(str(line))
    f.write("\n")

headers = {
    'Content-Type': 'application/json',
}

data = open('variants.json', 'rb').read()
response = requests.post('http://10.2.100.17:9200/_bulk', headers=headers, data=data)