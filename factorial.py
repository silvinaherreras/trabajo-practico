def factorial(n):
    print("factorial")
    if n== 0 or n == 1:
        resultado = 1
        print(resultado)
    elif n > 1:
        resultado = n * factorial(n-1)
        print(resultado)
    return resultado

#ress=factorial(4)
#print(ress)

def factorial2(num): 
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

#num = 5;
#print("Factorial of",num,"is", factorial2(num)) 



 