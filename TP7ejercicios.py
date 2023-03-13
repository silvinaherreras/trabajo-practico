def ejercicio1():
    """Cree un script para mostrar los primeros 100 números enteros positivos,
comenzando desde el 1."""
"""Modifique el script del ejercicio anterior para que se muestren sólo los números
pares. Para saber si un número es par, utilice el operador de módulo (%)."""
for i in range(1,101):
    if (i%2==0):
        print(i,",", end="")
def ejercicio3():
    """Cree un script para calcular el resultado de sumar los números desde el 75 al
150."""
    sumatoria=0
    sumatoria=sum([i for i in range(75,150)])
    return sumatoria
def ejercicio6():
    """Cree un script que le solicite al usuario ingresar 10 números, y una vez
ingresados, le muestre en pantalla cuál es el máximo, y en qué posición lo
ingresó. Por ejemplo, si el usuario ingresa los números 2, 63, -3, 20, 55, 89, 7, 32, 9,
y 33, se le debería mostrar el mensaje “El mayor número ingresado es 89, y lo
ingresaste en la posición 6”. NOTA: las posiciones posibles comienzan desde 1.
"""
def mayor():
    lista = [3,6,8,2,6]
    max = lista[0];
    
    for x in range(0,len(lista)):
        if lista[x] > max:
            max = lista[x]
            
    return max, lista.index(max)

#x,pos=mayor()
#print(x,pos)

#heights = [100, 2, 300, 10, 11, 1000]
#max_height = max(heights)
#print(max_height,heights.index(max_height))




