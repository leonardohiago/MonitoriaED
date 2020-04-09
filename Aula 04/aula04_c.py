def main():

    matriz = [
        [39,14,27],
        [21,83,92],
        [31,12,43]
    ]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == (len(matriz[i])-1):
                matriz[i].remove(matriz[i][j])

    print(matriz)

main()