import requests
import json

# endereço do swagger: https://petstore.swagger.io/

url = 'https://petstore.swagger.io/v2/'
id_pet = 45641848


# Método para ler o Json (assim não é necessário se preocupar se o arquivo foi fechado da memória, pois o método fecha.)
def ler_json(caminho):
    with open(caminho, 'rb') as arquivo:
        dados = arquivo.read()  # adicionar o arquivo em uma variável, para depois retorná-la
        return dados  # assim o arquivo pode fechar normalmente


def teste_incluir_pet():
    nome_esperado = 'Kuro'
    tag1_esperada = 'pequeno'
    tag2_esperada = 'preto'
    status_esperado = 'available'
    category_id_esperado = 2
    category_name_esperado = 'gato'
    status_code_esperado = 200
    headers = {'Content-Type': 'application/json'}

    resposta = requests.post(url=f'{url}pet',
                             data=ler_json('pet1.json'),
                             headers=headers)

    print(resposta)  # Response: Status Code
    print(resposta.status_code)  # Status Code
    corpo_resposta = resposta.json()  # variável que salva o body da resposta
    print(json.dumps(corpo_resposta, indent=4))  # Corpo da Resposta

    assert resposta.status_code == status_code_esperado
    assert corpo_resposta['name'] == nome_esperado
    assert corpo_resposta['status'] == status_esperado
    assert corpo_resposta['tags'][0]['name'] == tag1_esperada  # Primeiro elemento dentro da lista
    assert corpo_resposta['tags'][1]['name'] == tag2_esperada  # Segundo elemento dentro da lista
    assert corpo_resposta['category']['id'] == category_id_esperado  # Separa-se as tags por colchetes
    assert corpo_resposta['category']['name'] == category_name_esperado


def teste_consultar_pet():
    resposta_esperada = json.loads(ler_json('pet1.json'))  # subir um arquivo Json em uma variável
    # é usando loads e não load pois estamos lendo uma string e não um file/arquivo ('s' de string)

    # da forma abaixo o arquivo não é fechado com close, o ideal é fazer da forma acima
    # resposta_esperada = json.load(open('pet1.json', 'rb'))
    # print(json.dumps(resposta_esperada, indent=4))

    status_code_esperado = 200
    headers = {'Content-Type': 'application/json'}

    resposta = requests.get(url=f'{url}pet/{id_pet}',
                            headers=headers)

    corpo_resposta = resposta.json()
    print(json.dumps(corpo_resposta, indent=4))

    assert resposta.status_code == status_code_esperado
    assert corpo_resposta == resposta_esperada  # comparar resposta recebida com a variável criada anteriormente


def teste_atualizar_pet():
    dados = {
        'id': id_pet,
        'category': {
            'id': 2,
            'name': 'gato'
        },
        'name': 'Kuro',
        'photoUrls': [
            'https://i.pinimg.com/236x/26/aa/ac/26aaacc5810c544f7ebc70148451aa25--exorcist-anime-ao-no-exorcist-kuro'
            '.jpg'],
        'tags': [
            {
                'id': 1,
                'name': 'pequeno',
            },
            {
                'id': 2,
                'name': 'preto'
            },
            {
                'id': 3,
                'name': 'chocolate'
            }
        ],
        'status': 'available'
    }
    headers = {'content-type': 'application/json'}
    status_code_esperado = 200

    resposta = requests.put(url=f'{url}pet',
                            data=json.dumps(dados),
                            headers=headers)

    corpo_resposta = resposta.json()
    print(json.dumps(corpo_resposta, indent=4))

    assert resposta.status_code == status_code_esperado
    assert corpo_resposta == dados


def testar_deletar_usuario():
    headers = {'content-type': 'application/json'}
    status_code_esperado = 200

    resposta = requests.delete(url=f'{url}pet/{id_pet}',
                               headers=headers)

    corpo_resposta = resposta.json()
    print(json.dumps(corpo_resposta, indent=4))

    assert resposta.status_code == status_code_esperado
    assert corpo_resposta['code'] == status_code_esperado
    assert corpo_resposta['message'] == str(id_pet)
