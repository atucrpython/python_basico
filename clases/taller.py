""""
             |     |
             |     |
-------------       ---------
  x  x  x  x
-------------|      |----------
             |      |
"""



class Casilla:
    carro_dentro = None

    def esta_vacia(self):
        return True

    def agregarme(self, carro):
        self.carro_dentro = carro

    def __str__(self):
        dev = "vacio"
        if self.carro_dentro is not None:
            dev="lleno"
        return dev


class Carro:

    def __init__(self, marca, valor=1000):
        self.marca = marca
        self.valor = valor

    def avanzar_adelante(self, casilla):
        if casilla.esta_vacia():
            casilla.agregarme(self)
        else:
            self.chocar()

    def chocar(self):
        self.valor -= 100

micarro = Carro("BMW")
misegundocarro = Carro("Toyota")
carretera = []
for x in range(10):
    carretera.append(Casilla())

for encarretera in carretera:
    micarro.avanzar_adelante(encarretera)

# construcción de una instancia de la clase Casilla
micasilla = Casilla()
