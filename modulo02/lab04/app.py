def saludo():
    global nombre
    nombre = "John joe"
    print(f'Hola{nombre}')

    def despedida():
        #global nombre
        nombre="Sara Swan"
        print(f"adios{nombre}")

        saludo()
        despedida()
        print(nombre)
                  