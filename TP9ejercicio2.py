def is_primo(n):

    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True


def primos(lista):
    primos=list()
    for i in range(lista.len):
        if is_primo(lista[i]):
            primos.append((lista[i]))
    return primos

def sumatoria_promedio(lista):
    sumatoria=sum(lista)
    promedio=sumatoria/len(lista)
    return sumatoria,promedio

def factorial(num): 
    if num < 0: 
        print("Factorial of negative num does not exist")
    elif num == 0: 
        return 1        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 
    
def factoriales(lista):
    fatoriales=list()
    for i in range (lista.len ):
        factoriales.append(factorial(lista[i]))
    return factoriales

