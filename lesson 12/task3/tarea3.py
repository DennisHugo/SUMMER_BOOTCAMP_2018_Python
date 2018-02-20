from pygeocoder import Geocoder
import os

"""
geocoder.py
"""

if __name__ == '__main__':
    autor = os.getenv('AUTOR')
    print(autor)
    direccion = 'Escuela Militar de Ingenieria'
    print(Geocoder.geocode(direccion)[0].coordinates)
