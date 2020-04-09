def main():

    paises = []
    cidades = []

    i = 1

    while (i != 0):

        paises.append(str(input("Digite o nome de um país: ")))
        i = int(input("Deseja cadastrar mais algum país? 1 - Sim / 0 - Não "))

    j = int(input("Digite a quantidade de cidade que deseja cadastrar: "))

    for i in range(j):
        cidades.insert(i, str(input("Digite o nome de uma cidade: ")))

    print('Países: ', paises)
    print('Cidades: ', cidades)

main()