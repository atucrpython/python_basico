

class MiClase:
    valor = None
    decremento = None
    def __init__(self, valor):
        self.valor = valor
        self.decremento = int(valor*0.2)

    def __repr__(self):
        """ Es la representación del objecto """
        return "Miclase(%s)"%(self.valor,)

    def __le__(self, other):
        """ Compara con menor o igual que"""
        return self.valor-self.decremento <= other

    def __gt__(self, other):
        """ Compara con mayor que """
        return self.valor > other.valor

    def __cmp__(self, other):
        """
        Compara uno contra otro para saber si es mayor, menor o igual que
        Retorno:
            1 -> si es mayor
            0 -> si es igual
            -1 -> si es menor

        """
        if self.valor == other.valor:
            return 0
        if self.valor >= other.valor:
            return 1
        return -1

milista = [MiClase(7), MiClase(5), MiClase(10)]
milista.sort()
print(milista)