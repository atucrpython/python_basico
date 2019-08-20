def imprime_piramide(base):
    for x in range(1, base+1):
        print(" "*(base-x)+"*"*x)

def imprime_piramide_comentado(base):
    for x in range(1, base+1):
        espacios = " "*(base-x)
        asterisco = "*"*x
        print(espacios+asterisco+" -- "+str(len(espacios))+","+str(len(asterisco))+" -> "+str(len(espacios+asterisco)))

#userbase = int(input("Escriba el tamaño de la base: "))
imprime_piramide(8)