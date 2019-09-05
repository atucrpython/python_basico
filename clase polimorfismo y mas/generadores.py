
class Casa:
    def valor(self):
        return 200
class Carro:
    def valor(self):
        return 400

class Helado:
    def valor(self):
        return 700

class Generadora:
    def get_class_instance(self, nombre):
        if nombre == 'casa':
            return Casa()
        elif nombre == 'carro':
            return Carro()
        elif nombre == 'helado':
            return Helado()

midicGenerador = {
    'casa': Casa,
    'carro': Carro,
    'helado': Helado
}

micasa = midicGenerador['casa']()

migeneradora = Generadora()
micasa = migeneradora.get_class_instance('casa')
print(micasa.valor())