def mostrar_titulo():
    print('>> Calculadora de Fósforo <<')
    print('Defina a quantidade de Caixas de Fósforo:')


def calcular_fosforos(entrada):
    resultado = entrada * 40
    if type(entrada) != int:
        letras = 'Só aceito Números Inteiros!'
        print(letras)
        return letras
    elif entrada < 0:
        numero_negativo = 'Você NÃO pode colocar números negativos'
        print(numero_negativo)
        return numero_negativo
    elif entrada == 0:
        numero_zero = f'Com {entrada} Caixas você NÃO possui fósforos'
        print(numero_zero)
        return numero_zero
    elif entrada == 1:
        print(f'Você possui {entrada} Caixa e {resultado} fósforos')
        return resultado
    else:
        print(f'Você possui {entrada} Caixas e {resultado} fósforos')
        return resultado


if __name__ == '__main__':
    while True:
        mostrar_titulo()
        digitar = input()
        if digitar.lstrip('-').isdigit():   # também é possível usar o .replace('-', '') para substituir
            calcular_fosforos(int(digitar))
        else:
            calcular_fosforos(digitar)

        sair = input('Você quer calcular novamente? Digite S para continuar.\n')
        if sair.upper() == "S":
            continue
        else:
            print('Valeu!')
        break
