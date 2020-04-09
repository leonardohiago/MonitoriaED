def main():

    array = []

    for i in range(5):
        array.append(str(input("Digite um nome: ")))

    print(array)

    for i in range(len(array)):
        if "Leonardo" in array[i]:
            array.insert(i, "Hiago")
            break

    print(array)

main()