numero = int(input())
def ehPrimo(numero):
    if numero != 0 & numero != 1:
        if numero > 3:
            for i in range(2, numero):
                if numero % i == 0:
                    return 'Faina'
                else:
                    return 'Faina'
                    
        
    return 'Emidio'
print(ehPrimo(numero))
