import requests
from readCsv import extractorCeps
from calculateDistance import coordinatesFinder, coordinatesFinder

cepOrigen = extractorCeps()[1]

ibgeOrigem = []
ibgeDestino = []

for cep in cepOrigen:
    if cep != 'CEP_Origem':
        cep = coordinatesFinder(cep)
        url = 'https://viacep.com.br/ws/'+ cep[0] +'/json/'
        try:
            res = requests.get(url).json()
            ibgeOrigem.append(res['ibge'])
        except:
            ibgeOrigem.append(None)

        


