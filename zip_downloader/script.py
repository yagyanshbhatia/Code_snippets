import requests, zipfile, io
zip_file_url = input()
r = requests.get(zip_file_url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()