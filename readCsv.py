import csv


def extractorCeps():
    with open('base.csv', encoding='utf-8') as base:

        table = csv.reader(base, delimiter=';')

        cepDestinos = []
        cepOrigens = []
        nuPedidos = []

        for i in table:
            cepDestino = i[1]
            cepOrigem = i[6]
            nuPedido = i[2]
            cepDestinos.append(cepDestino)
            cepOrigens.append(cepOrigem)
            nuPedidos.append(nuPedido)

    return cepDestinos, cepOrigens, nuPedidos
