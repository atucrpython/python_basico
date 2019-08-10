# def nombre de la función ( ARGUMENTOS ) :
def ingrese_valor(mensaje, func):
    procesar = True
    while procesar:
        try:
            valor = input(mensaje)
            valor = func(valor)
            procesar = False
        except:
            print("Lo ingresado no corresponde a un tipo valido")
    return valor

figgeometricas = {
    'Cuadrado': ('Lado', ),
    'Circulo': ('Radio', ),
    'Rombo': ('Diagonal mayor', 'Diagonal menor'),
    'Rectangulo': ('Base', 'Altura'),
    'Triangulo': ('Base', 'Altura')
}

# Función para verificar lo que el usuario ingresa
# está en el diccionario
def esta_en_figgeometricas(texto):
    texto = texto.capitalize()
    # global nos permite utilizar una variable que está fuera
    # del ámbito de la función
    global figgeometricas
    if texto not in figgeometricas:
        raise # lanzo un excepción si lo que el usuario
              # ingresó no está en el diccionario figgeometricas
    return texto

def solicita_attr_figura(campos):
    # campos siempre es un iterador
    dev = []
    for campo in campos:
        dev.append(ingrese_valor(
            "Digite el valor de %s :"%campo, int
        ))
    return dev

# pido al usuario la figura a calcular
resultado = ingrese_valor(
    "¿Cúal figura (%s)?: "%(
        ", ".join( figgeometricas.keys())
    ), esta_en_figgeometricas )
# pido los campos de la figura
print(solicita_attr_figura(
    figgeometricas[resultado])
    )
