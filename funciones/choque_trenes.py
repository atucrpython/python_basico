tren1 = int(input("Velocidad tren 1: "))
tren2 = int(input("Velocidad tren 2: "))
distancia = int(input("Distancia: "))

rep_distancia = [0]*distancia
posicion_tren1 = 0
posicion_tren2 = len(rep_distancia)-1
tiempo = 0
seguir = True
while seguir:
    tiempo += 1
    for mov_tren1 in range(tren1):
        if rep_distancia[posicion_tren1] != 0:
            seguir = False
            break
        rep_distancia[posicion_tren1] = 1
        posicion_tren1+=1
    if seguir:
        for mov_tren2 in range(tren2):
            if rep_distancia[posicion_tren2] != 0:
                seguir = False
                break
            rep_distancia[posicion_tren2] = 2
            posicion_tren2 -= 1

print(rep_distancia)
print("Los trenes chocan en el km "+str(tiempo*tren1))