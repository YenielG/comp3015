def busqueda_secuencial(lista, palabras):
    for i in range(len(lista)):
        if lista[i] == palabras:
            return True 
    return False 

lista_de_palabras = ["BMW", "TOYOTA", "ACURA", "NISSAN", "PORCHE"]
palabras = "BMW"
resultado = busqueda_secuencial(lista_de_palabras, palabras)
if resultado:
    print("La palabra", palabras, "se encuentra en la lista.")
else:
    print("La palabra", palabras, "no se encuentra en la lista.")
