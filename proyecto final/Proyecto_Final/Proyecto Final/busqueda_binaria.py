def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio  
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  

# lista ordenada
lista_binaria = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20,22,24,26,28,30,32]

# Valor  buscar
buscar_valor = 30

resultado = busqueda_binaria(lista_binaria, buscar_valor)

# Verificar el resultado
if resultado != -1:
    print(f"El valor {buscar_valor} se encuentra en la posición {resultado}.")
else:
    print(f"El valor {buscar_valor} no se encuentra en la lista.")
