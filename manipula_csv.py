""" Arquivo com funcoes de manipulacao de csv """
import csv


def adjust_data(k, val):
    """ Devine o tipo de variavel deve ser retornado """
    if k == 'id':
        return int(val)
    if k == 'nome':
        return val
    if k == 'valor':
        return float(val)
    if k == 'tipo':
        return val
    if k == 'disposicao':
        return int(val)

    return val


def csv2json(filename):
    """ Converte um arquivo csv para lista de dicionarios """
    with open(filename) as file:
        output = [{k: adjust_data(k, val) for k, val in row.items()}
            for row in csv.DictReader(file, skipinitialspace=True)]

    return output


def atualiza_csv(filename, linha, coluna, valor):
    """ Atualiza uma célula do arquivo csv """
    read = csv.reader(open(filename))
    lines = list(read)

    lines[linha][coluna] = valor

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)
