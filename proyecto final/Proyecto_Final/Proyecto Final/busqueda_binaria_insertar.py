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

lista_binaria = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]

buscar_valor = 30

resultado = busqueda_binaria_insertar(lista_binaria, buscar_valor)

if resultado < len(lista_binaria) and lista_binaria[resultado] == buscar_valor:
    print(f"El valor {buscar_valor} se encuentra en la posición {resultado}.")
else:
    print(f"El valor {buscar_valor} no se encuentra en la lista. Se puede insertar en la posición {resultado}.")

