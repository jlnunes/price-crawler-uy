import requests as r
import json

search_word = 'leche entera conaprole'
url = 'http://www.devoto.com.uy/' + search_word

response = r.get(url)


text = response.text
str_to_find = 'vtex.events.addData'
index = text.find(str_to_find)+len(str_to_find)+1
line = ''
while True:
    if text[index] == ")":
        break
    else:
        line = line + text[index]
        index = index +1

line = line.encode('ascii','ignore')
line = json.loads(line)

for product in line['shelfProductIds']:
    print product