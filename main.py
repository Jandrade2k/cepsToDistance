import csv
import time
from readCsv import extractorCeps
from test import rota
from calculateDistance import coordinatesFinder

extrato = extractorCeps()

cepDestinos = extrato[0]
cepOrigens = extrato[1]
nuPedidos = extrato[2]

for destino in cepDestinos:
    time.sleep(2)
    cep = coordinatesFinder(destino)
    if cep == None or cep == 'CEP Destino':
        destino = None

for origem in cepDestinos:
    time.sleep(2)
    cep = coordinatesFinder(origem)
    if cep == None or cep == 'CEP_Origem':
        origem = None

result = []

file = open('./base copy.csv', 'w')

for i in range(len(cepDestinos)):
    print('baixando dados '+i+' de '+len(cepDestinos))
    time.sleep(2)
    if cepDestinos[i] == None or cepDestinos[i] == 'CEP Destino':
        result.append(None)
    elif cepOrigens[i] == None or cepDestinos[i] == 'CEP_Origem':
        result.append(None)
    else:
        fin = rota(cepOrigens[i], cepDestinos[i])

        if fin == None:
            result.append(fin)
        else:
            result.append(fin.text)
            writer = csv.writer(file)
            writer.writerow(fin.text)
