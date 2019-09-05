
class MiDiccionario:
    y = 1
    x = 0
    z = 10
    def __getitem__(self, item):
        if item == 'y':
            return self.y
        elif item == 'x':
            return self.x
        elif item == 'z':
            return self.z
        return "No hay nada"


midic = MiDiccionario()
print(
    midic['z'],
    midic['y'],
    midic['x'],
    midic['hola']
)