from readCsv import extractorCeps
from municipios import municipios

cepOrigem = extractorCeps()[1]
cepDestino = extractorCeps()[0]

def findCEP(cep):
    for municipio in municipios:
        if municipio['codigo_ibge'] == cep:
            return municipio

def coordinatesFinder(cep):
    ibge = []
    if len(cep) > 8:
        cep = cep[0:8]
    elif len(cep) < 8:
        while len(cep) < 8:
            cep+='0'
    ibge.append(cep)
    return ibge


