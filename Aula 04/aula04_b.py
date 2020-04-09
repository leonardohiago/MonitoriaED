def main():

    matriz = [[39, 14, 27], [21, 83, 92], [31, 12, 43]]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'Posição: {i, j} | Valor: {matriz[i][j]} | Valor *7: {(matriz[i][j])*7}')
            if j == (len(matriz[i])-1):
                matriz[i].remove(matriz[i][j])

main()