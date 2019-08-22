
def cuenta_regresiva(numero):
    print("Iniciando cuenta regresiva: ", numero)
    if numero > 0:
        cuenta_regresiva(numero-1)
    else:
        print("Terminando recursión por condición de parada")

    print("Finalizando cuenta regresiva: ", numero)

cuenta_regresiva(5)