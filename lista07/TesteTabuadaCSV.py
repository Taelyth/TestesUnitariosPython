import csv
import sys

import pytest

from lista06.tabuada.tabuada import checagem_de_caracteres, tabuada


def ler_dados_do_csv():
    teste_dados_csv = []
    nome_arquivo = 'tabuada.csv'
    try:
        with open(nome_arquivo, newline='', encoding='utf-8') as csvfile:
            dados = csv.reader(csvfile, delimiter=',')
            next(dados)
            for linha in dados:
                teste_dados_csv.append(linha)
        return teste_dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except csv.Error as exception:
        sys.exit('file {}, line {}: {}'.format(nome_arquivo, dados.line_num, exception))
    except Exception as exception:
        print(f'Falha imprevista: {exception}')


class TesteTabuadaCSV:

    @pytest.mark.parametrize('parametro, resultado_esperado', ler_dados_do_csv())
    def teste_tabuada_csv(self, parametro, resultado_esperado):
        if parametro.isdigit():
            assert str(checagem_de_caracteres(int(parametro))) == resultado_esperado
            assert str(tabuada(int(parametro))) == resultado_esperado
        elif parametro.lstrip('-').isdigit():
            assert str(checagem_de_caracteres(int(parametro))) == resultado_esperado
        else:
            assert checagem_de_caracteres(parametro) == resultado_esperado
