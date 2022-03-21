import csv


def extractorCeps():
    with open('base.csv', encoding='utf-8') as base:

        table = csv.reader(base, delimiter=';')

        cepDestinos = []
        cepOrigens = []

        for i in table:
            cepDestino = i[1]
            cepOrigem = i[6]
            cepDestinos.append(cepDestino)
            cepOrigens.append(cepOrigem)
    return cepDestinos, cepOrigens
