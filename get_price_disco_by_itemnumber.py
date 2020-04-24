import requests as r
import json

item_n=31741
url ='https://www.disco.com.uy/api/catalog_system/pub/products/search/?&fq=productId:'+str(item_n)
response = r.get(url)

data = response.json()[0]
#lista = data['items'][0]['sellers'][0]['commertialOffer']['Price']
price = response.json()[0]['items'][0]['sellers'][0]['commertialOffer']['Price']
print price