class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass
    def es_domestico(self):
        return False
    def get_nombre(self):
        return self.nombre

class AnimalCasero:
    def get_nombre(self):
        return "Casero: "+self.nombre

class Gato(AnimalCasero, Animal):
    def hacer_sonido(self):
        return "Miau"
    def es_domestico(self):
        return True
class Leon(Animal):
    def hacer_sonido(self):
        return "rugido..."

class Tigre(Animal):
    pass

migato = Gato("Misingo")
mileon = Leon("Simba")
print(migato.get_nombre(), migato.es_domestico())
print(mileon.hacer_sonido(), mileon.es_domestico())
