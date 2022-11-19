import urllib.request
opener = urllib.request.build_opener()
response = opener.open ('https://en.wikipedia.org/wiki/Main_Page')
print(response.read())

import requests

response = requests.get('https://www.youtube.com/')
print(response.text)
print(f"Datatype - {type(response.content)}")

response = requests.post('https://remanga.org/', data='Test', headers = {'h1': 'TITLE'})
print(response.text)
res_parse_list = []
response = requests.get('https://coinmarketcap.com/')
response_text = response.text
response_parse = response_text.split("<span>")
for pars_elem_1 in response_parse:
    if pars_elem_1.startswith('$'):
        for pars_elem_2 in pars_elem_1.split("</span>"):
            if pars_elem_2.startswith('$') and pars_elem_2[1].isdigit():
                res_parse_list.append(pars_elem_2)
bitcoin = res_parse_list[0]
print(bitcoin)