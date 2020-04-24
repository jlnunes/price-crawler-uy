import requests as r
import json


def D_search_by_string(search_word='',supermercado='Disco'):
    
    if supermercado=='Disco':
        web = 'http://www.disco.com.uy/' 
    else: web = 'http://www.devoto.com.uy/'
    
    url = web + search_word
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
    
    return line['shelfProductIds']


def D_get_price_by_product_number(product_n=0, supermercado='Disco'):
    
    if supermercado=='Disco':
        web = 'http://www.disco.com.uy/' 
    else: web = 'http://www.devoto.com.uy/'
    
    
    url = web + 'api/catalog_system/pub/products/search/?&fq=productId:'+str(product_n)
    response = r.get(url)
    output = {}
    data = response.json()[0]
    price = data['items'][0]['sellers'][0]['commertialOffer']['Price']
    output ['Precio'] = price
    output ['Nombre'] = data['productName']
    return output