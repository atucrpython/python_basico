from random import randint

def num_entre_ellos(numero1, numero2, cantidad):
    if numero2 < numero1:
        tmp = numero1
        numero1 = numero2
        numero2 = tmp
    lista =[]
    for x in range(cantidad):
        lista.append(randint(numero1, numero2))

    return lista

num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))
cantidad = int(input("cantidad: "))
print(num_entre_ellos(num1, num2, cantidad))
