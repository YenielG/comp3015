def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  
        
    return -1  

lista = [231, 355, 231, 193, 112, 137]
objetivo = 112
resultado = busqueda_secuencial(lista, objetivo)
print("El objetivo", objetivo, "se encuentra en la posición de la lista:", resultado)
