def lee_opcion():
    """Solicita una opción de menú y la devuelve."""
    opcion_invalida = True
    while opcion_invalida:
        opcion = input("Ingrese A (Altas) - B (Bajas) - M (Modificaciones): ")
       
        opcion = opcion.upper()
        if (opcion == "A" or opcion == "B" or opcion == "M"):
            opcion_invalida = False
        else:
            print(f'La tecla {opcion} no es una opción válida.')
    return opcion

lee_opcion()