def num_entre_ellos(numero1, numero2):
    if numero2 < numero1:
        tmp = numero1
        numero1 = numero2
        numero2 = tmp

    for x in range(numero1+1, numero2):
        print(x)

num_entre_ellos(61, 100)
num_entre_ellos(35, 21)