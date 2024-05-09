import random

def lista_aleatoria(cantidad):
    return [random.randint(1, 100) for _ in range(cantidad)]

def busqueda_binaria_insertar(lista, valor_objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == valor_objetivo:
            return medio  
        elif lista[medio] < valor_objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return izquierda  

lista = sorted(lista_aleatoria(20))

objetivo = int(input("Ingrese un número para buscar en la lista: "))

resultado = busqueda_binaria_insertar(lista, objetivo)

if resultado < len(lista) and lista[resultado] == objetivo:
    print(f"El número {objetivo} se encontró en la posición {resultado} de la lista.")
else:
    print(f"El número {objetivo} no se encontró en la lista. Va insertarse en la posición {resultado}.")

