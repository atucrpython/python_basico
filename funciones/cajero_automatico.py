# 10 000, 5 000, 2 000

def calc_nombre(cantidad):
    dev = "billetes"
    if cantidad == 1:
        dev = "billete"
    return dev

correr = True
while correr:
    valor = input("Que desea hacer t transacción s salir")
    if valor.lower() == 's':
        correr = False
    elif valor.lower() == 't':
        monto = int(input("Digite el monto: "))
        div5000 = monto%5000
        billete5000 = monto // 5000
        if div5000 == 1000 or div5000 == 3000:
            billete5000 = billete5000 - 1
        monto = monto - billete5000*5000
        if monto % 2000 != 0:
            print("Usted digitó un monto incorrecto")
        billete2000 = monto // 2000
        billete10000 = billete5000 // 2
        if billete10000 != 0:
            billete5000 = billete5000 - billete10000*2

        print("Su dinero es %d %s de 2000, %.2f %s de 5000 y %d %s de 10 000 "%(
            billete2000,
            calc_nombre(billete2000),
            billete5000,
            calc_nombre(billete5000),
            billete10000,
            calc_nombre(billete10000)
        ))


