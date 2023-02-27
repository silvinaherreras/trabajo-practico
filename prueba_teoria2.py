def mayor_de_3(numero1,numero2,numero3):
    if(numero1>=2) and (numero1>=3):
        return numero1
    elif (numero2>numero1) and (numero2>=3):
        return numero2
    else:
        return numero3
    
print (mayor_de_3(1,2,2))
print (mayor_de_3(2,2,3))
print (mayor_de_3(5,5,3))
print (mayor_de_3(2,10,10))
print (mayor_de_3(2,10,10))