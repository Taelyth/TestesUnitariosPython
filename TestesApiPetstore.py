import pytest
import requests
import json

# endereço do swagger: https://petstore.swagger.io/

url = 'https://petstore.swagger.io/v2/'
id_usuario = 4781678


@pytest.mark.order(1)  # biblioteca pytest-order do pip, serve para ordenar os testes
def testar_incluir_usuario():
    # Configura
    status_code_esperado = 200
    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.post(f'{url}user',
                             data=open('json/usuario1.json', 'rb'),
                             headers=headers)
    print(resposta)  # Response: Status Code
    print(resposta.status_code)  # Status Code
    corpo_resposta = resposta.json()  # variável que salva o body da resposta
    print(json.dumps(corpo_resposta, indent=4))  # Corpo da Resposta

    # Valida
    assert resposta.status_code == status_code_esperado  # Código de comunicação
    assert corpo_resposta['code'] == status_code_esperado  # Código na funcionalidade
    assert corpo_resposta['message'] == str(id_usuario)


@pytest.mark.order(2)
def testar_consultar_usuario():
    # Configura
    username = 'Testinho'
    status_code_esperado = 200
    headers = {'Content-Type': 'application/json'}
    email_esperado = 'testinho@batata.com.br'
    firstname_esperado = 'Batata'

    # Executa
    resposta = requests.get(f'{url}user/{username}',
                            headers=headers)
    print(resposta)
    print(resposta.status_code)
    corpo_resposta = resposta.json()
    print(json.dumps(corpo_resposta, indent=4))

    # Valida
    assert resposta.status_code == status_code_esperado  # Código de comunicação
    assert corpo_resposta['id'] == id_usuario
    assert corpo_resposta['username'] == username
    assert corpo_resposta['firstName'] == firstname_esperado
    assert corpo_resposta['email'] == email_esperado


@pytest.mark.order(4)
def testar_atualizar_usuario():
    # Configura
    username = 'Testinho'
    headers = {'content-type': 'application/json'}
    dados = {
        'id': id_usuario,
        'username': username,
        'firstName': 'Batata',
        'lastName': 'Frita',
        'email': 'frita@batata.com.br',
        'password': 'batata123',
        'phone': '11988888888',
        'userStatus': 0
    }
    status_code_esperado = 200

    # Executa
    resposta = requests.put(url=f'{url}user/{username}',
                            data=json.dumps(dados),
                            headers=headers)
    print(resposta)
    print(resposta.status_code)
    corpo_resposta = resposta.json()
    print(json.dumps(corpo_resposta, indent=4))

    # Valida
    assert resposta.status_code == status_code_esperado  # Código de comunicação
    assert corpo_resposta['code'] == status_code_esperado  # Código na funcionalidade
    assert corpo_resposta['message'] == str(id_usuario)


@pytest.mark.order(5)
def testar_deletar_usuario():
    # Configura
    username = 'Testinho'
    headers = {'content-type': 'application/json'}
    status_code_esperado = 200

    # Executa
    resposta = requests.delete(url=f'{url}user/{username}',
                               headers=headers)
    print(resposta)
    print(resposta.status_code)
    corpo_resposta = resposta.json()
    print(json.dumps(corpo_resposta, indent=4))

    # Valida
    assert resposta.status_code == status_code_esperado  # Código de comunicação
    assert corpo_resposta['code'] == status_code_esperado  # Código na funcionalidade
    assert corpo_resposta['message'] == username


def consultar_usuario_extrair_senha(username):
    # Configura
    status_code_esperado = 200
    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.get(f'{url}user/{username}',
                            headers=headers)

    corpo_resposta = resposta.json()

    # Valida
    assert resposta.status_code == status_code_esperado  # Código de comunicação
    return corpo_resposta['password']


def login(username, password):
    headers = {'Content-Type': 'application/json'}
    mensagem_esperada = 'logged in user session:'
    status_code_esperado = 200

    # https://petstore.swagger.io/v2/user/login?username=a&password=a

    resposta = requests.get(f'{url}user/login?username={username}&password={password}',
                            headers=headers)

    corpo_resposta = resposta.json()

    token = corpo_resposta['message'].rpartition(':')[-1]

    assert resposta.status_code == status_code_esperado  # Código de comunicação
    assert mensagem_esperada in corpo_resposta['message']
    return token


@pytest.mark.order(3)
def testar_consulta_e_login():
    # vai orquestrar a chamada da consulta e login do usuário
    username = 'Testinho'
    token = login(username, consultar_usuario_extrair_senha(username))
    print(f'Token no maestro: {token}')
