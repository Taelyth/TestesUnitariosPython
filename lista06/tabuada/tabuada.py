def tabuada(numero):
    soma = 1
    print('-' * 10)
    print(f'Tabuada de {numero}')
    print('-' * 10)
    lista = []

    # loop da tabuada com while:
    while soma <= 10:
        # print(f'{soma} x {numero} = {soma * numero}')
        lista.append(soma * numero)
        print(f'{soma} x {numero} = {lista[soma - 1]}')
        soma += 1
    return lista

    # Também é possível fazer o loop da tabuada com o for:
    # for soma in range(1, 11):
    #     lista.append(soma * numero)
    #     print(f'{soma} x {numero} = {lista[soma - 1]}')
    #     soma += 1
    # return lista


def checagem_de_caracteres(texto):
    if type(texto) != int:
        letras = 'Só aceito Números Inteiros!'
        print(letras)
        return letras
    elif texto < 0:
        numero_negativo = 'Você NÃO pode colocar números negativos'
        print(numero_negativo)
        return numero_negativo
    else:
        return tabuada(texto)


if __name__ == '__main__':
    digitar = input('Digite o número que deseja saber a tabuada: ')
    while True:
        # digitar = input('Digite o número que deseja saber a tabuada: ')
        if digitar.lstrip('-').isdigit():
            checagem_de_caracteres(int(digitar))
        else:
            checagem_de_caracteres(digitar)

        # Primeira idéia:
        # sair = input('\nVocê quer ver a tabuada de outro número? Digite S para continuar.\n')
        # if sair.upper() == 'S':
        #     continue
        # else:
        #     print('Valeu!')
        #     break

        # idéia melhorada:
        sair = input('\nPara saber outra tabuada digite um número, se quiser sair digite S\n')
        if sair.upper() != 'S':
            digitar = sair
            continue
        else:
            print('Valeu!')
            break
