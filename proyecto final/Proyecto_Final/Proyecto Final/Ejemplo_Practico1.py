import random
#Utilice radiant para generar numeros aletorios mas facil
def generar_lista_aleatoria(cantidad):
    return [random.randint(1, 100) for _ in range(cantidad)]

def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

lista = generar_lista_aleatoria(20)

objetivo = int(input("Ingrese un número para buscar en la lista: "))

resultado = busqueda_secuencial(lista, objetivo)

if resultado != -1:
    print(f"El número {objetivo} se encontró en la posición {resultado} de la lista.")
else:
    print(f"El número {objetivo} no se encontró en la lista.")
