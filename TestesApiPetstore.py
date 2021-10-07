import requests
import json

# endereço do swagger: https://petstore.swagger.io/

url = 'https://petstore.swagger.io/v2/'
id_usuario = 4781678


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
