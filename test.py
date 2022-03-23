from unittest import result
import requests
import json
import time

def rota(cep1, cep2):

    cep1 = cep1.replace('-', '')
    cep2 = cep2.replace('-', '')
    time.sleep(2)
    url1 = 'https://viacep.com.br/ws/' + cep1 + '/json/'
    url2 = 'https://viacep.com.br/ws/' + cep2 + '/json/'

    req1 = requests.get(url1)
    req2 = requests.get(url2)

    if req1.status_code == 200 and req2.status_code == 200:

        origem = json.loads(req1.text)
        destino = json.loads(req2.text)

        try:

            strOrigem = origem['localidade'] + ' ' + origem['uf']
            strOrigem = strOrigem.replace(' ', '+')

            strDestino = destino['localidade'] + ' ' + destino['uf']
            strDestino = strDestino.replace(' ', '+')

            return requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins='
                            +strOrigem+'&destinations='+strDestino+'&key=AIzaSyCNS3O-fdNpBzrphRJvIXGwkxQhxoe9oBk')
        except:
            return None

    else :
        return None