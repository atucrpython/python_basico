N = int(input("Escriba la cantidad de discos: "))

lorigen=list(range(1, N+1))
lintermedio = []
lfinal=[]

def hanoi(N, origen, intermedio, final):
    if N > 0: 
        hanoi(N-1, origen, final, intermedio)
        final.append(origen.pop())
        print("%r %r %r"%(lorigen, lintermedio, lfinal) )
        hanoi(N-1, intermedio, origen, final) 

hanoi(N, lorigen, lintermedio, lfinal)
