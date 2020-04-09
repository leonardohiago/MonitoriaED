def main():

    array = ["azul", "verde", "laranja", "vermelho", "rosa"]

    for i in range(len(array)):
        if "vermelho" in array:
            array.remove("vermelho")

    print(array)

main()