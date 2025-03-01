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

"Programa 2: Ordenacion de arreglo multidimensionales"
# Crear una matriz 3x3
matriz = [
    [10, 20, 30],
    [90, 50, 60],
    [70, 80, 40]
]

def bubble_sort(fila)
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila [j+1], fila[j]

def ordenar_fila(matriz, fila_numero):
    fila = matriz [fila_numero]
    print(f"Matriz orginal:\n{matriz}")
    bubble_sort(fila)
    print(f"Matriz despues de ordenar la fila{fila_numero}:\n{matriz}")


ordenar_fila(matriz,1)




