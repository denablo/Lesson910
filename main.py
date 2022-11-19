import urllib.request
opener = urllib.request.build_opener()
response = opener.open ('https://en.wikipedia.org/')
print(response.read())

import requests

response = requests.get('https://www.youtube.com/')
print(response.content)
print(f"Datatype - {type(response.content)}")
