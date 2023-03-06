def ejercicio1():
    """Cree un script para mostrar los primeros 100 números enteros positivos,
comenzando desde el 1."""
"""Modifique el script del ejercicio anterior para que se muestren sólo los números
pares. Para saber si un número es par, utilice el operador de módulo (%)."""
for i in range(1,101):
    if (i%2==0):
        print(i,",", end="")

#ejercicio1()
def ejercicio3():
    """Cree un script para calcular el resultado de sumar los números desde el 75 al
150."""
    sumatoria=0
    sumatoria=sum([i for i in range(75,150)])
    return sumatoria

#print (ejercicio3())

