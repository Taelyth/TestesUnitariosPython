# 1 - imports - bibliotecas
import pytest


# 2 - class - classe


# 3 - definitions - definições = métodos e funções
def print_hi(name):
    print(f'Oi, {name}')  # O f serve para chamar o parâmetro da função


def somar(numero1, numero2):
    return numero1 + numero2


def subtrair(numero1, numero2):
    return numero1 - numero2


def multiplicar(numero1, numero2):
    return numero1 * numero2


def dividir(numero1, numero2):
    if numero2 != 0:
        return numero1 // numero2
    else:
        return 'Não pode dividir por Zero'


def dividir_try_except(numero1, numero2):
    try:
        return numero1 // numero2
    except ZeroDivisionError:
        return 'Não pode dividir por Zero'
    # finally:
    #     print("Codigo rodou")


# Testes Unitários / Teste de Unidades
# Teste Parametrizado
@pytest.mark.parametrize('numero1,numero2,resultado_esperado', [
    # valores
    (5, 4, 9),  # teste 1
    (3, 2, 5),  # teste 2
    (10, 6, 16),  # teste 3
    (10, 6, 15)  # teste 4
])
def test_somar_parametrizado(numero1, numero2, resultado_esperado):
    try:
        assert somar(numero1, numero2) == resultado_esperado
    except AssertionError:
        print(f'Entrou no Except: {AssertionError}')
    finally:
        print('Código rodou')
# O try/except não é usado muito para testes, mas sim pra programação.
# Para fazer testes negativos, é melhor utilizar os asserts para as mensagens de erro


# teste da função somar
def test_somar():
    # 1 - Configura / Prepara
    numero1 = 8  # input / entrada
    numero2 = 5  # input / entrada
    resultado_esperado = 13  # output / saída

    # 2 - Executa
    resultado_atual = somar(numero1, numero2)

    # 3 - Checa / Valida
    assert resultado_atual == resultado_esperado
    print(f'\nO resultado atual é: {resultado_atual}\nO resultado esperado é: {resultado_esperado}')


# o mesmo teste, mas resumido
def test_somar_compacto():
    assert somar(8, 5) == 13


def test_subtrair_compacto():
    assert subtrair(4, 5) == -1


def test_multiplicar_compacto():
    assert multiplicar(4, 3) == 12


def test_dividir_compacto():
    assert dividir(8, 2) == 4


def test_dividir_por_zero_compacto():
    assert dividir(8, 0) == 'Não pode dividir por Zero'


@pytest.mark.parametrize('num1, num2, resultado_esperado', [
    (8, 4, 2),
    (8, 0, 'Não pode dividir por Zero'),
    (20, 4, 5)
])
def test_dividir_try_except(num1, num2, resultado_esperado):
    assert dividir_try_except(num1, num2) == resultado_esperado


if __name__ == '__main__':
    print_hi('Jaque')

    # soma de 2 números
    resultado = somar(5, 6)
    print(f'O resultado da soma é: {resultado}')

'''
    # subtração de 2 números
    resultado = subtrair(5, 3)
    print(f'O resultado da subtração é: {resultado}')

    # multiplicação
    resultado = multiplicar(2, 4)
    print(f'O resultado da multiplicação é: {resultado}')

    # divisão
    resultado = dividir(4, 2)
    print(f'O resultado da divisão é: {resultado}')
'''
