def ejercicio5():
    """Cree un script que, dado un número de día de la semana ingresado por
teclado, muestre el nombre de ese día en lenguaje natural. La relación entre
números y días de la semana es la siguiente:
1 = Domingo.
2 = Lunes.
3 = Martes.
4 = Miércoles.
5 = Jueves.
6 = Viernes.
7 = Sábado."""
try:
    dia=int(input("Ingrese dia de la semana "))
    if (dia==1):
        print("Domingo")
    elif (dia==2):
        print("Lunes")
    elif (dia==3):
        print ("Martes")
    elif (dia==4):
        print ("Miércoles")
    elif (dia==5):
        print ("Jueves")
    elif (dia==6):
        print ("Viernes")
    elif (dia==7):
        print ("Sábado")
    else:
        print ("no es un diá de la semana")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    print ("no es un diá de la semana")


def ejercicio6():
    """Cree un script que le solicite a un alumno de la asignatura Introducción a la
Programación que ingrese las notas de sus dos parciales. Como resultado, se
le debe informar al alumno su situación, junto con la nota promedio. Las
reglas para saber la situación de un alumno son las siguientes:
● Para estar promovido (es decir, cursada aprobada y no requiere
rendir final), el alumno debe haber aprobado ambos parciales y
tener un promedio mayor o igual a 8.
● Para estar regular (cursada aprobada, pero debe rendir final), el
alumno debe haber aprobado ambos parciales (nota mayor o igual
a 4).
● Si el alumno no ha aprobado ambos parciales (es decir, tiene nota
menor que 4 en alguno de ellos), entonces queda en condición de
libre (es decir, puede rendir un final extendido o recursar)."""
try:
    nota1=float(input("Ingrese nota1"))
    nota2=float(input("Ingrese nota2"))
    resultado=nota1+nota2/2
    if (nota1>=4) and (nota2>=4):
         if (resultado>=8):
            print ("promovido")
         else:
            print ("reugular")
    else:
         print("Libre")

   
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")

ejercicio6()
   


