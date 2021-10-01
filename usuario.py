# 1 - imports
import sys

import pytest
import csv
import json

import requests
from requests import HTTPError


# teste_dados_novos_usuarios = [
#     (1, 'Juca', 'Pirama', 'juca@iterasys.com.br'),  # usuário 1
#     (2, 'Agatha', 'Christie', 'agatha@iterasys.com.br')  # usuário 2
# ]

teste_dados_usuarios_atuais = [
    (1, 'George', 'Bluth', 'george.bluth@reqres.in'),
    (2, 'Janet', 'Weaver', 'janet.weaver@reqres.in')
]


# CRUD / ICAE
# Aplicações            API         Português
# Create                Post        Incluir
# Reach / Research      Get         Consultar / Pegar
# Update                Put         Atualizar
# Delete                Delete      Excluir


@pytest.mark.parametrize('id_esperado, nome, sobrenome, email', teste_dados_usuarios_atuais)
def testar_dados_usuarios(id_esperado, nome, sobrenome, email):  # função que testa o algo
    try:
        response = requests.get(f'https://reqres.in/api/users/{id_esperado}')
        json_response = response.json()
        id_obtido = json_response['data']['id']
        nome_obtido = json_response['data']['first_name']
        sobrenome_obtido = json_response['data']['last_name']
        email_obtido = json_response['data']['email']

        print(json.dumps(json_response, indent=2, sort_keys=True))

        assert response.status_code == 200
        assert id_obtido == id_esperado
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email

    except HTTPError as http_error:
        print(f'Um erro de HTTP aconteceu: {http_error}')
    except Exception as exception:
        print(f'Falha inesperada: {exception}')

# função que faz algo --> fora do meu computador
# API que vamos usar para fazer o teste:
# https://regres.in/api/users/{id}
# Documentação: https://reqres.in/


def ler_dados_do_csv():
    teste_dados_csv = []
    nome_arquivo = 'usuarios.csv'
    try:
        with open(nome_arquivo, newline='') as csvfile:
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


@pytest.mark.parametrize('id_esperado, nome, sobrenome, email', ler_dados_do_csv())
def testar_dados_usuarios_csv(id_esperado, nome, sobrenome, email):  # função que testa o algo
    try:
        response = requests.get(f'https://reqres.in/api/users/{id_esperado}')
        json_response = response.json()
        id_obtido = json_response['data']['id']
        nome_obtido = json_response['data']['first_name']
        sobrenome_obtido = json_response['data']['last_name']
        email_obtido = json_response['data']['email']

        print(json.dumps(json_response, indent=2, sort_keys=True))

        assert response.status_code == 200
        assert id_obtido == int(id_esperado)
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email

    except HTTPError as http_error:
        print(f'Um erro de HTTP aconteceu: {http_error}')
    # except Exception as exception:
    #     print(f'Falha inesperada: {exception}')
