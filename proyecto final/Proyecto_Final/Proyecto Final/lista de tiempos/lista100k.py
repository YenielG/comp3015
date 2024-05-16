import random
import time

# Creación de las listas
lista_pequena = [random.randint(0, 1000000) for _ in range(1001)]
lista_mediana = [random.randint(0, 1000000) for _ in range(50001)]
lista_grande = [random.randint(0, 1000000) for _ in range(1000001)]

# Búsqueda Secuencial
def busqueda_secuencial(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return None

# Búsqueda Binaria
def busqueda_binaria(lista, item):
    low = 0
    high = len(lista) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lista[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# Medición de tiempo
def medir_tiempo(lista, busqueda_func):
    inicio = time.time()
    busqueda_func(lista, lista[-1]) # Buscamos el último elemento para el peor caso
    fin = time.time()
    return fin - inicio

print("Tiempo Búsqueda Secuencial Lista Pequeña: ", medir_tiempo(lista_pequena, busqueda_secuencial))
print("Tiempo Búsqueda Binaria Lista Pequeña: ", medir_tiempo(sorted(lista_pequena), busqueda_binaria))
print("Tiempo Búsqueda Secuencial Lista Mediana: ", medir_tiempo(lista_mediana, busqueda_secuencial))
print("Tiempo Búsqueda Binaria Lista Mediana: ", medir_tiempo(sorted(lista_mediana), busqueda_binaria))
print("Tiempo Búsqueda Secuencial Lista Grande: ", medir_tiempo(lista_grande, busqueda_secuencial))
print("Tiempo Búsqueda Binaria Lista Grande: ", medir_tiempo(sorted(lista_grande), busqueda_binaria))
