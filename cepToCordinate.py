import pycep_correios
from geopy.geocoders import Nominatim
from readCsv import extractorCeps

coordDestinos = extractorCeps()[0]
coordOrigens = extractorCeps()[1]

def coordinatesDestinos():

    arr = []

    for i in coordDestinos:
        if i != 'CEP Destino':
            if len(i) < 7:
                while len(i) < 8:
                    i.append('0')
            i = i.replace('-', '')
            address = pycep_correios.get_address_from_cep(i)
            geolocator = Nominatim(timeout=1, user_agent='datime')
            logradouro = address['logradouro'].split(' - ')[0]
            if logradouro == None:
                logradouro = address['logradouro']
            location = geolocator.geocode(logradouro + ", " + address['cidade'] + " - "+ address['bairro'])
            arr.append(location)
    return arr

def coordinatesOrigens():

    arr = []
    for i in coordOrigens:
        if i != 'CEP_Origem':
            arr.append()
    return arr
