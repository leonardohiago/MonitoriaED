def main():

    array = []

    i = 1

    while (i != 0):
        array.append(float(input("Digite um valor: ")))
        i = int(input("Deseja cadastrar mais algum valor? 1 - Sim / 0 - Não "))

    print('\nOs valores digitados foram: ', array)

main()