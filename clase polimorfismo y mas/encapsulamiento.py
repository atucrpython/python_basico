class Ejemplo:
    __miattr = 30
    # Esta función puede llamarse desde cualquier parte
    def publico(self):
        print("Función publica")
    # Esta función no puede ser llamada desde el exterior
    def __privado(self):
        print("Función privada")

    # Desde un método de la clase si puedo llamar a una
    # función privada
    def privada(self):
        self.__privado()

miejemplo = Ejemplo()
miejemplo.publico()
miejemplo.privada()
# Esto provoca un error indicando que no existe el atributo
print(miejemplo.__miattr)