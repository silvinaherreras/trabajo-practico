import TP5ejercicios
def ejercicio3():
    """ Cree un script que almacene, en dos variables, una base y un exponente, y
    luego muestre en pantalla el resultado de elevar el número base a la
    potencia exponente."""
    numero=int(input('ingrese número'))    
    exponente=int(input('ingrese exponente'))
    resultado=numero**exponente
    print(f' el resultado de elevar el {numero} a la base  {exponente} es :{resultado} ')

#ejercicio3()
def ejercicio4():
    """Implemente un algoritmo en Python para calcular el perímetro de un
    rectángulo, conociendo su base y altura. Los datos se deben almacenar en
    variables, y el resultado se debe mostrar en pantalla.
    perímetro = 2 * (base + altura)"""
    base=int(input('ingrese número '))    
    altura=int(input('ingrese altura '))
    resultado=2 * (base + altura)
    print(f' el resultado  es :{resultado} ')

#ejercicio4()

def ejercicio5(base,altura):
    """Implemente un algoritmo en Python para calcular el área de un rectángulo,
    conociendo su base y altura. Los datos se deben almacenar en variables, y el
    resultado se debe mostrar en pantalla.
    área = base * altura"""
    resultado=base * altura
    print(f' el área  es :{resultado} ')

#ejercicio5(4,6)

def ejercicio7(a,b):
    """En Python es posible resolver el problema del intercambio de valores sin
    hacer uso de variables adicionales, mediante la sintaxis de asignación
    múltiple. Investigue de qué se trata dicha funcionalidad, y utilízela para
    resolver el ejercicio anterior sin utilizar variables auxiliares/adicionales."""
    print(f'el valor de a {a} el valor de b {b}')
    a,b=b,a
    print(f'el valor de a {a} el valor de b {b}')
#ejercicio7(2,3)

def ejercicio8():
    """Escriba un algoritmo que, conociendo las notas de los dos parciales de un
alumno de la asignatura Introducción a la Programación, muestre en
pantalla su promedio."""
    notas=[]
    cantidad_notas=int(input("ingrese cantidad materias: "))
    for i in range (cantidad_notas):
        nota=float(input("nota: "))
        notas.append(nota)

    promedio=sum(notas)/len(notas)
    print(f'El promedio es: {promedio}')

#ejercicio8()


 
def ejercicio9(pesos): 
    """Cree un script que, sabiendo cuántos pesos argentinos tiene una persona
ahorrada en su cuenta (almacenando ese monto en una variable), muestre
en pantalla los montos convertidos en dólares (U$1 = $80.5), reales ($R1 =
$14.1), y euros (€1 = $69.5). La salida del programa debe tener el siguiente
formato:"""
    dolares=pesos*80.5
    modenda_dolar = "U${:,.2f}".format(dolares)   
    reales=pesos*14.1
    modenda_reales = "R${:,.2f}".format(reales)   
    euros=pesos*69.5
    modenda_euros = "€{:,.2f}".format(euros)       
    aux="""Usted tiene ${} pesos argentinos, los cuales se convierten en:
    - {} dólares.
    - {} reales.
    - €{} euros."""
    print(aux.format(pesos,modenda_dolar,modenda_reales,modenda_euros))

#ejercicio9(65.5)
#print (ejercicio7("silv","si"))
print(TP5ejercicios.ejercicio8())

    


