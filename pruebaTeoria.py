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

#lee_opcion()
def Problema81 ():
    """
    Queremos escribir un programa que nos permita armar la lista de los inscriptos
    de una materia.
    Mantenimiento: No permitir que haya legajos repetidos.
    Mantenimiento: Permitir guardar el nombre y apellido de los estudiantes."""
    print("Inscripciones al curso de Introducción a la Programación")
    inscriptos=[]
    datos_personales=[]
    centinela=input("ingrese legajo para terminar ingrese *")
    while centinela !="*":
        if centinela in inscriptos:
            print(f"el legajo {centinela} ya esta inscripto")
        else:
            inscriptos.append(centinela)
            nombre_apellido=input("Ingrese el nombre y apellido: ")
            datos_personales.append(nombre_apellido)
        centinela=input("ingrese legajo para terminar ingrese *")
    return inscriptos,datos_personales
  

def imprimirInscriptos(inscriptos,datos_personales):
    for posicion,legajo in enumerate( inscriptos):
        print(posicion,legajo,datos_personales[posicion])



def ej():
    aux = 5 % 2 == 0
    aux2 = "hola"
    aux3 = str.__contains__(aux2, "a")
    aux0 = "a"
    print("si ", aux2 in aux0)
    print(aux2.capitalize())
    d = "@Una@cadena@con@arrobas"
    aux4 = d.split("@")
    print(aux4)
    aux5 = "&".join(aux4)
    print(aux4)
    print(aux5)
    ejlstrip = "siiiilvina hola probando"
    aux6 = ejlstrip.lstrip("si")
    print(aux6)
    string = "++++x...y!!z* geeksforgeeks"
    # Removes given set of characters from left.
    print(string.lstrip("+.!*xyz"))
# ej()


def ejercicio_web():
    # Create a sample collection
    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

    # Strategy:  Iterate over a copy
    for user, status in users.copy().items():
        if status == 'inactive':
            del users[user]

    # Strategy:  Create a new collection
    active_users = {}
    for user, status in users.items():
        if status == 'active':
            active_users[user] = status

    print (active_users)
ejercicio_web()

def main():
    legajos,datos_personales=Problema81()
    print("La lista de inscriptos es:",legajos)
    imprimirInscriptos(legajos,datos_personales)
    for i in range(len(legajos)):
        print(f"Inscripto {i}: ({legajos[i]}) {datos_personales[i]}")

main()