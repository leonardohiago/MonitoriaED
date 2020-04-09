import random

def main():

    lista = [1996, 1970, 1971, 1999, 2000]
    lista2 = [1996, 1970, 1971, 1999, 2000]

    lista_crescente = []
    lista_decrescente = []

    # código para ordenar "na mão"

    for i in range(len(lista)):
        menor = lista[0]
        for j in range(len(lista)):
            if lista[j] < menor:
                menor = lista[j]
                pos_menor = j
        lista_crescente.append(menor)
        lista.remove(menor)

    print('Do menor para o maior: ', lista_crescente)

    for k in range(len(lista2)):
        maior = lista2[0]
        for l in range(len(lista2)):
            if lista2[l] > maior:
                maior = lista2[l]
                pos_maior = l
        lista_decrescente.append(maior)
        lista2.remove(maior)

    print('Do maior para o menor: ', lista_decrescente)

    # código para ordenar "automático"

    lista3 = [1996, 1970, 1971, 1999, 2000]
    lista4 = [1996, 1970, 1971, 1999, 2000]

    lista3.sort()
    print('\nDo menor para o maior: ', lista3)

    lista4.sort(reverse=True)
    print('Do maior para o menor: ', lista4)


main()