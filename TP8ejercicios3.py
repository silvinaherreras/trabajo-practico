def ejercicio3():
    """Cree un script que le solicite al usuario leer un número entero entre 1 y 100. El
programa debe ser capaz de solicitarle al usuario que reingrese el número
cuantas veces sea necesario, hasta que el usuario provea un dato válido. Cada
vez que detecte un error de validación, informele al usuario cuál fue el error, con
los mensajes “El dato ingresado no es numérico.”, o “El número ingresado está
fuera del rango permitido.”. Finalmente, cuando el usuario ingrese un dato
válido, muestre el mensaje “[NÚMERO] es válido. Gracias!”."""

centinela=False
while not centinela:
    dato=input("ingrese número del 1 al 100 ")
    if (dato.isdigit()):
        dato=int(dato)
        if (dato>=1) and (dato<=100):
            print(f"{dato} es válido. Gracias!")
            centinela=True
        else:
            print("El número ingresado está fuera del rango permitido")
                
    else:
        print ("El dato ingresado no es numérico.")