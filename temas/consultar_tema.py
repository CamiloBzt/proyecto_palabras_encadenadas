from temas.mostrar_temas import traer_temas
from procedimientos.validando import valid_pala_2, valid_num, valid_selec
import json


def consul_pala(ruta: str) -> None:
    """
    Función que permite al usuario consultar las palabras de un tema.
    :param ruta: ruta del archivo de temas.
    """
    print(''.center(40, '-'))
    print(' CONSULTAR'.center(40, '-'))
    print(' PALABRAS '.center(40, '-'))
    print(''.center(40, '-'))
    print(' Seleccione el tema '.center(40, '-'))
    print(''.center(40, '-'))
    print(' Digite 1 si lo quiere elegir '.center(40, '-'))
    print(' enter de lo contrario '.center(40, '-'))
    print(''.center(40, '-'))
    sure = None
    temas = traer_temas(ruta)
    # Ciclo que va hasta que el usuario este seguro de su decisión.
    while sure != '1':
        tema = None
        while not tema:
            for llave in temas:
                if not tema:
                    print(''.center(40, '-'))
                    print(llave.center(40))
                    print(''.center(40, '-'))
                    selec = input()
                    selec = valid_selec(selec)
                    if selec == '1' and selec != '':
                        tema = llave
            if not tema:
                print(''.center(40, '-'))
                print(' Por favor, seleccione un tema '.center(40, '-'))
                print(''.center(40, '-'))
                print(''.center(40, '-'))
                print(' Si quiere salir presione enter '.center(40, '-'))
                print(' De lo contrario 1'.center(40, '-'))
                selec = input()
                selec = valid_selec(selec)
                if selec == '':
                    tema = 'salir'
                    sure = '1'
            if tema != 'salir' and tema is not None:
                print(''.center(40, '-'))
                print(' Su tema es {} '.center(40).format(tema))
                print(''.center(40, '-'))
                print(''.center(40, '-'))
                print(' Si esta seguro de su tema '.center(40, '-'))
                print(' digite 1 de lo contrario enter '.center(40, '-'))
                print(''.center(40, '-'))
                sure = input()
                sure = valid_selec(sure)
                if sure != '':
                    palabras = temas.get(tema)
                    print(''.center(40, '-'))
                    print(' Las palabras del tema {} '.center(40).format(tema))
                    print(' son: '.center(40, '-'))
                    print(''.center(40, '-'))
                    for palabra in palabras:
                        print(palabra)
                else:
                    tema = None
    print(''.center(40, '-'))
    print(' Gracias  '.center(40, '-'))
    print(' presione enter para volver '.center(40, '-'))
    print(''.center(40, '-'))
    enter = input()
    while enter != '':
        print(''.center(40, '-'))
        print(' presione enter para volver '.center(40, '-'))
        print(''.center(40, '-'))
        enter = input()


def consul_pala_2(ruta: str) -> None:
    """
    Función que permite al usurio ingresar una palabra y decir si pertenece
    o no al tema, si la palabra no esta en los temas, el usuario tiene la
    opción de agregarla.
    :param ruta: ruta del archivo de temas.
    """
    print(''.center(40, '-'))
    print(' CONSULTAR'.center(40, '-'))
    print(' SI PALABRA '.center(40, '-'))
    print(' EXISTE '.center(40, '-'))
    print(''.center(40, '-'))
    print(' Seleccione el tema '.center(40, '-'))
    print(''.center(40, '-'))
    print(' Digite 1 si lo quiere elegir '.center(40, '-'))
    print(' enter de lo contrario '.center(40, '-'))
    print(''.center(40, '-'))
    sure = None
    temas = traer_temas(ruta)
    while sure != '1':
        tema = None
        while not tema:
            for llave in temas:
                if not tema:
                    print(''.center(40, '-'))
                    print(llave.center(40))
                    print(''.center(40, '-'))
                    selec = input()
                    selec = valid_selec(selec)
                    if selec == '1' and selec != '':
                        tema = llave
            if not tema:
                print(''.center(40, '-'))
                print(' Por favor, seleccione un tema '.center(40, '-'))
                print(''.center(40, '-'))
                print(''.center(40, '-'))
                print(' Si quiere salir presione enter '.center(40, '-'))
                print(' De lo contrario 1'.center(40, '-'))
                selec = input()
                selec = valid_selec(selec)
                if selec == '':
                    tema = 'salir'
                    sure = '1'
            if tema != 'salir' and tema is not None:
                print(''.center(40, '-'))
                print(' Su tema es {} '.center(40).format(tema))
                print(''.center(40, '-'))
                print(''.center(40, '-'))
                print(' Si esta seguro de su tema '.center(40, '-'))
                print(' digite 1 de lo contrario enter '.center(40, '-'))
                print(''.center(40, '-'))
                sure = input()
                sure = valid_selec(sure)
                if sure != '':
                    palabras = temas.get(tema)
                    print(''.center(40, '-'))
                    print(' Digite el numero de palabras '.center(40, '-'))
                    print(' a consultar '.center(40, '-'))
                    print(''.center(40, '-'))
                    num = input()
                    num = valid_num(num)
                    for i in range(num):
                        print(''.center(40, '-'))
                        print(' Digite la palabra de su tema {} '.center(40).format(tema))
                        print(' ha verificar '.center(40, '-'))
                        print(''.center(40, '-'))
                        palabra = input()
                        palabra = valid_pala_2(palabra)
                        if palabra in palabras:
                            print(''.center(40, '-'))
                            print(' Su palabra esta en  '.center(40, '-'))
                            print(' su tema {} '.center(40).format(tema))
                            print(''.center(40, '-'))
                        elif palabra not in palabras:
                            print(''.center(40, '-'))
                            print(' Su palabra no esta en  '.center(40, '-'))
                            print(' su tema {} '.center(40).format(tema))
                            print(''.center(40, '-'))
                            print(''.center(40, '-'))
                            print(' Desea agregar?  '.center(40, '-'))
                            print(' Digite 1 de lo contrario enter '.center(40, '-'))
                            print(''.center(40, '-'))
                            add = input()
                            add = valid_selec(add)
                            if add == '1':
                                palabras.append(palabra)
                    temas[tema] = palabras
                    temas = json.dumps(temas, indent=3)
                    archivo = open(ruta, "w")
                    archivo.write(temas)
                    archivo.close()
                else:
                    tema = None
    print(''.center(40, '-'))
    print(' Gracias  '.center(40, '-'))
    print(' presione enter para volver '.center(40, '-'))
    print(''.center(40, '-'))
    enter = input()
    while enter != '':
        print(''.center(40, '-'))
        print(' presione enter para volver '.center(40, '-'))
        print(''.center(40, '-'))
        enter = input()


def cant_pala(ruta: str) -> None:
    """
    Función que le permite saber al usuario la cantidad
    de palabras en un tema.
    :param ruta: ruta del archivo de temas.
    """
    print(''.center(40, '-'))
    print(' CONSULTAR'.center(40, '-'))
    print(' CANTIDA DE '.center(40, '-'))
    print(' PALABRAS '.center(40, '-'))
    print(''.center(40, '-'))
    print(' Seleccione el tema '.center(40, '-'))
    print(''.center(40, '-'))
    print(' Digite 1 si lo quiere elegir '.center(40, '-'))
    print(' enter de lo contrario '.center(40, '-'))
    print(''.center(40, '-'))
    sure = None
    temas = traer_temas(ruta)
    while sure != '1':
        tema = None
        while not tema:
            for llave in temas:
                if not tema:
                    print(''.center(40, '-'))
                    print(llave.center(40))
                    print(''.center(40, '-'))
                    selec = input()
                    selec = valid_selec(selec)
                    if selec == '1' and selec != '':
                        tema = llave
            if not tema:
                print(''.center(40, '-'))
                print(' Por favor, seleccione un tema '.center(40, '-'))
                print(''.center(40, '-'))
                print(''.center(40, '-'))
                print(' Si quiere salir presione enter '.center(40, '-'))
                print(' De lo contrario 1'.center(40, '-'))
                selec = input()
                selec = valid_selec(selec)
                if selec == '':
                    tema = 'salir'
                    sure = '1'
            if tema != 'salir' and tema is not None:
                print(''.center(40, '-'))
                print(' Su tema es {} '.center(40).format(tema))
                print(''.center(40, '-'))
                print(''.center(40, '-'))
                print(' Si esta seguro de su tema '.center(40, '-'))
                print(' digite 1 de lo contrario enter '.center(40, '-'))
                print(''.center(40, '-'))
                sure = input()
                sure = valid_selec(sure)
                if sure != '':
                    palabras = temas.get(tema)
                    cant = len(palabras)
                    print(''.center(40, '-'))
                    print(' La cantidad de palabras'.center(40, '-'))
                    print(' de su tema {} '.center(40).format(tema))
                    print(' es de {} palabras '.center(40).format(cant))
                    print(''.center(40, '-'))
                else:
                    tema = None
    print(''.center(40, '-'))
    print(' Gracias  '.center(40, '-'))
    print(' presione enter para volver '.center(40, '-'))
    print(''.center(40, '-'))
    enter = input()
    while enter != '':
        print(''.center(40, '-'))
        print(' presione enter para volver '.center(40, '-'))
        print(''.center(40, '-'))
        enter = input()
