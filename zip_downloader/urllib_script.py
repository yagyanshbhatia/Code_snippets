import requests
import urllib.request

url = input()

print("downloading with urllib.request")
urllib.request.urlretrieve(url, "code.zip")

print("downloading with requests")
r = requests.get(url)
with open("code3.zip", "wb") as code:
    code.write(r.content)