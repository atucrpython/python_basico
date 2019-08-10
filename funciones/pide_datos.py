def valida_si_no(texto):
    texto = texto.lower()

    if texto not in ['si', 'no' ]:
        raise
    return texto

# def nombre de la función ( ARGUMENTOS ) :
def ingrese_valor(mensaje, func, x):
    procesar = True
    while procesar:
        try:
            valor = input(mensaje)
            valor = func(valor)
            procesar = False
        except:
            print("Lo ingresado no corresponde a un tipo valido")
    return valor

nombre = ingrese_valor("Digite su nombre: ", str, 78)
edad = ingrese_valor("Digite la edad: ", int, 50)
casado = ingrese_valor("Está casado (si, no)", valida_si_no, 67)
print(nombre,  edad, casado)

