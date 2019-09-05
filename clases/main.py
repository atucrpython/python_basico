
class Pizzara:
    def __init__(self):
        self.pendientes = []

    def agregar(self, carro):
        self.pendientes.append(carro)

    def eliminar(self, carro):
        pos =  self.pendientes.index(carro)
        if pos > 0:
            del self.pendientes[pos]

    def save(self):
        with open("pizarra.txt", "w") as archivo:
            for carro in self.pendientes:
                archivo.write("%s, %r\n"%(carro.marca,
                                          carro.lista_reparaciones))

class Carro:
    def __init__(self, marca, lista_reparaciones):
        self.marca = marca
        self.lista_reparaciones = lista_reparaciones


a1 = Carro("BMW", ['reparar aires'])
a2 = Carro("Audi", ['cambiar aires'])
a3 = Carro("Purdi", ['cambiar tapones'])

pizarra = Pizzara()

pizarra.agregar(a1)
pizarra.agregar(a2)
pizarra.save()