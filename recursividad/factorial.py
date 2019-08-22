
def factorial(numero):
    valor_ingresado = numero
    #print("Inicial ", numero)
    #condición de parada
    if numero>1:
        numero = numero * factorial(numero-1)
        #siempre después de llamar a una función se retorna
        # a la posición del llamado
    else:
        numero = 1
    print("Factorial de %d = %d"%(valor_ingresado, numero))
    return numero

factorial(6)