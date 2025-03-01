# Definimos una matriz 3x3 de ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def buscar_en_matriz(valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"El valor {valor} fue encontrado en la posición ({i}, {j})"
    return f"El valor {valor} no se encuentra en la matriz."


valor_a_buscar = 5


print(buscar_en_matriz(valor_a_buscar))

#

