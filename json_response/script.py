url = "https://github.com/yagyanshbhatia/Code_snippets/raw/master/json_response/manifest.json"
import urllib.request

data = urllib.request.urlopen(url) # read only 20 000 chars

s = str(data.read())[2:-1]

import json


json_data = json.loads(s)
print(json_data)
