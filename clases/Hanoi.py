N=4
lista_origen = [4,3,2, 1]
lista_intermedio = []
lista_final = []

# final = [4,3,2,1]

def hanoi(N, origen, intermedio, final ):
    if N > 0:
        hanoi(N-1, origen, final, intermedio)
        final.append(origen.pop())
        #print(">> %r %r %r"%(origen, intermedio, final))
        print("%r %r %r"%(lista_origen, lista_intermedio, lista_final) )
        hanoi(N - 1,intermedio, origen, final)

hanoi(N, lista_origen, lista_intermedio, lista_final)

# origen 1 al intermedio
# origen 2 al final
# intermedio 1 al final
# origen 3 al intermedio
# final al origen
# final a intermedio
# origen al intermedio
# origen al final
# intermedio al final
# intermedio al origen
# final al intermedio
# intermedio al origen
# intermedio al final
# origen al intermedio
# origen al final
# intermedio a final



