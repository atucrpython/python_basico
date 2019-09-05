class InterfazObjComprable:
    def get_valor(self):
        pass

    def comprar(self):
        pass

class Casa(InterfazObjComprable):
    def get_valor(self):
        return 100
    def comprar(self):
        print("Gracias por compra una casa")

class Carro(InterfazObjComprable):
    def get_valor(self):
        return 300
    def comprar(self):
        print("Gracias por compra un carro")

class Heladeria:
    def get_valor(self):
        return 900
    def comprar(self):
        print("Que rico helado")


# Funcion polimorfica, define una interfaz de comunicación con las clases
def comprar_bien(objeto):
    print(objeto.__class__.__name__ )
    # Comparo si el objeto es hijo de una clase
    if isinstance(objeto, InterfazObjComprable):
        print("bingo")
    # Verifico si existe el atributo o 
    # método en un objeto
    if hasattr(objeto, 'get_valor'):
        if 200 > objeto.get_valor():
            objeto.comprar()


if __name__ == '__main__':
    micasa = Casa()
    comprar_bien(micasa)
    micarro = Carro()
    comprar_bien(micarro)
    mihelado = Heladeria()
    comprar_bien(mihelado)