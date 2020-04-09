def main():

    registros = []

    for i in range(5):
        registros.append(str(input("Digite um nome: ")))

    print(registros)

    registros.insert(1, str(input("Digite outro nome: ")))

    print(registros)

main()