#first line comment (added localy)
#now a second line comment
from disco_n_devoto_lib import D_search_by_string, D_get_price_by_product_number
from ti_lib import TI_search_by_string
import sys


#busqueda = 'Palta'
busqueda = sys.argv[1]
print '\nBuscando: ' +busqueda + '\n'

#DISCO
products_D = D_search_by_string(busqueda,'Disco')

print 'Disco\n'
for product in products_D:
    aux = D_get_price_by_product_number(product,'Disco')
    print aux['Nombre']+' : $ '+str(aux['Precio'])

#DEVOTO
products_D = D_search_by_string(busqueda,'Devoto')

print '\nDevoto\n'
for product in products_D:
    aux = D_get_price_by_product_number(product,'Devoto')
    print aux['Nombre']+' : $ '+str(aux['Precio'])



products_TI = TI_search_by_string(busqueda)
print '\nTienda Inglesa\n'
for product in products_TI:
    print product['Producto']+' : '+product['Price']

print '\n'

