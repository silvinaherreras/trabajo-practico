def validacion():
    x=( input("ingrese cantidad"))
    if isinstance(x, float):
        print (x, ' es un número es real')
        x = int(x)
    else:
        print("El valor no es un número naturalw")
    x = "Error"

validacion()
    