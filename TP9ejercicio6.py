def ejercicio6():
    """Escribir una función que reciba una cadena a buscar y una lista de nombres
de personas y busque dentro de la lista, todas los elementos que contengan esa
cadena o cualquier parte de ella. Debe devolver una lista con los elementos
encontrados."""

lista= ["Mark", "Amber", "Todd", "Anita", "Sandy","andy","andrew"]
coincidencias=[]
a="san"
for i in range(len(lista)):    
    if (a in lista[i].lower()):
        coincidencias.append(lista[i])

print(coincidencias)