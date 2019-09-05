from collections import OrderedDict


class H:
    def hola(self):
        print("Hola")

midic = {
    'hola': 'mundo',
    'patito': 30,
    'lista': [1,2,3,4,5,2],
    'clases': H(),
    'diccionario': {1:3, 4:5},
    20: "hola"
}

print(midic[20])

dicfuncion = {'arg1': 20, 'arg2': 50}
x = 30
if x > 20 :
    dicfuncion['arg3'] = 300
def mifuncion(arg1=None, arg2=39, arg3=90, arg4=1):
    print(arg1, arg2, arg3)

def miotrafuncion(*args, **kwargs):
    print(kwargs['arg1'])

lista = []
miotrafuncion(*lista, **dicfuncion)



"""
d = OrderedDict()
d['miclave'] = 0

midictionary = dict()
midictionary['a'] = 'b'

midic.update(midictionary)
midic['agregado'] = 200010
print(midic.get('patitow', 'no existe'))
print('patitow' in midic)

if 'patito' in midic:
    print(midic['patito'])
    midic['patito'] = 900
    print(midic['patito']+500)

print(  list(midic.keys()) )
print(  list(midic.values()) )

"""