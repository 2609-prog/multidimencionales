# Programa 2: Ordenación de Arreglo multidimensional

# Crear una matriz 3x3
matriz = [
    [10, 20, 30],
    [90, 50, 60],
    [70, 80, 40]
]

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

def ordenar_fila(matriz, fila_numero):
    fila = matriz[fila_numero]
    print(f"Matriz original:\n{matriz}")
    bubble_sort(fila)
    matriz[fila_numero] = fila
    print(f"Matriz después de ordenar la fila {fila_numero}:\n{matriz}")

ordenar_fila(matriz, 1)