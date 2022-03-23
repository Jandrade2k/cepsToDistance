import csv

header=['errados']

with open('base.csv', encoding='utf-8') as base:

        table = csv.reader(base, delimiter=';')

        clientesErrados = []

        file = open('./base copy.csv', 'w')

        writer = csv.writer(file)

        for i in table:
            if i[1] != 'CEP Destino':
                if len(i[1]) < 7 or len(i[6]) < 7:
                    clientesErrados.append('errados')
                    writer.writerow('ERRADO')
                else:
                    clientesErrados.append('certo')
                    writer.writerow('CERTO')
            else:
                writer.writerow(header[0])
        







