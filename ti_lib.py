import requests as r
import re
from bs4 import BeautifulSoup

def TI_search_by_string(search_word=''):
    url = 'https://www.tiendainglesa.com.uy/busqueda?0,0,' + search_word +',0'
    
    
    response = r.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    
    spans = soup.find_all('span')
    
    product_list=[]
    for span in spans:
        if span['class'][0] == 'wCartProductName':
            aux = span['id']
            product_list.append({'ID' : aux, 'Producto' : span.string, 'priceID' : re.sub("[A-z]*$",'PRICE',aux) })
    
    for i, product in enumerate(product_list):
        price = soup.find_all(id=product['priceID'])[0].string
        if price is None:
            price = soup.find_all(id=product['priceID'])[0].text
        product_list[i]['Price'] = price
    
    return product_list