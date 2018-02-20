from http import client
from urllib.parse import quote_plus
import json

"""
httpz://depelopers.google.com/maps/documentation/
"""

def geocode(address):
    #format url
    hostname = 'maps.google.com'
    base = '/maps/api/geocode/json'
    add_plus = quote_plus(address)
    direccion = '{}/address={}'.format(base,add_plus)
    print(hostname+direccion)
    #CONECCION Y METODO GET
    connection = client.HTTPConnection(hostname)
    connection.request('GET',direccion)
    #respuesta
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    result = reply['results']
    diccionario_base = result[0]
    address_components = diccionario_base['geometry']
    location = address_components['location']
    print(location)

if __name__ == '__main__':
    address = 'UMSS'
    geocode(address)
    address = 'CEIS UMSS (Centro de Estudiantes de Ingenieria de sistemas),'
    address += 'Cochabamba'
    geocode(address)
