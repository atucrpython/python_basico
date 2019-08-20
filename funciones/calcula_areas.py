# def nombre de la función ( ARGUMENTOS ) :
import math
do_run = True

def ingrese_valor(mensaje, func):
    procesar = True
    while procesar:
        try:
            valor = input(mensaje)
            valor = func(valor)
            procesar = False
        except Exception as e:
            print(e)
            print("Lo ingresado no corresponde a un tipo valido")
    return valor

figgeometricas = {
    'Cuadrado': ('Lado', ),
    'Circulo': ('Radio', ),
    'Rombo': ('Diagonal mayor', 'Diagonal menor'),
    'Rectangulo': ('Base', 'Altura'),
    'Triangulo': ('Base', 'Altura'),
    'Exit': []
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
    # campos siempre es una tupla
    dev = []
    for campo in campos:
        dev.append(ingrese_valor(
            "Digite el valor de %s :"%campo, int
        ))
    return dev


def calcula_el_area(valores, eltipo):
    """
    Calcula el área de las figuras soportadas

    :param valores: Es una lista de enteros usados según la figura
    :param eltipo:  Corresponde al nombre de la figura
    :return:  int - el area de la figura dada
    """
    resultado = 0
    if eltipo == 'Cuadrado':
        resultado = valores[0] * valores[0]
    elif eltipo == 'Circulo':
        resultado = valores[0] * valores[0] * math.pi
    elif eltipo == 'Rombo' or eltipo == 'Triangulo':
        resultado = (valores[0] * valores[1])/2
    elif eltipo == 'Rectangulo':
        resultado = valores[0] * valores[1]
    elif eltipo == 'Exit':
        global do_run
        do_run = False

    return resultado

def run():
    # pido al usuario la figura a calcular
    fig_seleccionada = ingrese_valor(
        "Cual figura (%s) o exit: "%( ", ".join( figgeometricas.keys()) ),
        esta_en_figgeometricas )
    # pido los campos de la figura
    valores = solicita_attr_figura(figgeometricas[fig_seleccionada])
    # Calculo el área de la figura
    area = calcula_el_area(valores, fig_seleccionada)
    # imprimo al usuario el resultado
    if fig_seleccionada != 'Exit':
        print("El área de %s es %.2f"%(fig_seleccionada, area) )

while do_run:
    run()