def ejercicio6(entradaUpper,entradaLower):
    """Cree una función que reciba un string como parámetro, y retorne el mismo
string, pero con todas las letras convertidas a mayúsculas.
Modifique la función del ejercicio anterior para que retorne dos versiones del
string recibido como parámetro: primero la versión en minúsculas, y luego la
versión en mayúsculas."""
    return  entradaUpper.upper(),entradaLower.lower()


#print(ejercicio6("hola","CHAU"))

def ejercicio7(nombre1,nombre2):
    """Cree una función que reciba dos string como parámetro (nombre1 y nombre2),
y retorne True si nombre1 tiene más letras que nombre2, o False en caso
contrario."""
    aux= len(nombre1)>len(nombre2)
    return aux
#print (ejercicio7("silvina","silv"))

def ejercicio8():
    """Cree un archivo llamado modulo_cadena.py; dentro de él, cree una función
llamada leer_cadena que, sin recibir ningún parámetro, le solicite al usuario leer
un string cualquiera, y luego lo retorne. Luego cree otro archivo llamado
programa_principal.py, que ejecute el programa haciendo uso de la función
creada en el otro archivo."""
    return input("ingreses nombre ")
def ej():
    aux=5%2==0
    aux2="hola"
    aux3=str.__contains__(aux2,"a")
    print(aux)
    print(aux3)
    print(aux2.capitalize())

ej()