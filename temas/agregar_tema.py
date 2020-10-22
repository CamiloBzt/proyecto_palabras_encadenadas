from temas.mostrar_temas import traer_temas
from procedimientos.validando import valid_num, valid_pala_2, valid_selec
import json


def copiar_exist(ruta: str) -> None:
    """
    Función que permite al usuario agregar mas palabras a un tema ya existente.
    :param ruta: ruta del archivo de temas.
    """
    print(''.center(40, '-'))
    print(' COPIAR DE TEMA'.center(40, '-'))
    print(' EXISTENTE '.center(40, '-'))
    print(''.center(40, '-'))
    print(' Seleccione el tema '.center(40, '-'))
    print(''.center(40, '-'))
    print(' Digite 1 si lo quiere elegir '.center(40, '-'))
    print(' enter de lo contrario '.center(40, '-'))
    print(''.center(40, '-'))
    temas = traer_temas(ruta)
    tema = None
    # Ciclo: Hasta que el usuario escoja un tema o salga.
    while not tema:
        for llave in temas:
            # Condición para que no muestre mas temas si
            # el usuario ya selecciono uno.
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
        if tema != 'salir' and tema is not None:
            print(''.center(40, '-'))
            print(' Su tema es {} '.center(40).format(tema))
            print(''.center(40, '-'))
            palabras = temas.get(tema)
            print(''.center(40, '-'))
            print(' Digite el numero de palabras '.center(40, '-'))
            print(' a ingresar'.center(40, '-'))
            print(''.center(40, '-'))
            num = input()
            num = valid_num(num)
            num = int(num)
            # Ciclo que va hasta el numero entero
            # de palabras que el usuario digito.
            for i in range(num):
                sure = None
                # Ciclo que va hasta que el usuario
                # este seguro de su palabra.
                while sure != '1':
                    print(''.center(40, '-'))
                    print(' Digite su palabra '.center(40, '-'))
                    print(''.center(40, '-'))
                    palabra = input()
                    palabra = valid_pala_2(palabra)
                    while palabra in palabras:
                        print(''.center(40, '-'))
                        print(' Palabra repetida '.center(40, '-'))
                        print(' digite otra'.center(40, '-'))
                        print(''.center(40, '-'))
                        palabra = input()
                        palabra = valid_pala_2(palabra)
                    print(''.center(40, '-'))
                    print(' Su palabra es {} '.center(40).format(palabra))
                    print(''.center(40, '-'))
                    print(' Si esta seguro de su palabra '.center(40, '-'))
                    print(' digite 1 de lo contrario enter '.center(40, '-'))
                    print(''.center(40, '-'))
                    sure = input()
                    sure = valid_selec(sure)
                    if sure == '1':
                        palabra = palabra.lower()
                        palabras.append(palabra)
            temas[tema] = palabras
            temas = json.dumps(temas, indent=3)
            archivo = open(ruta, "w")
            archivo.write(temas)
            archivo.close()

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


def create(ruta: str) -> None:
    """
    Función que permite al usuario crear un tema.
    :param ruta: ruta del archivo de temas.
    """
    dic_temas = traer_temas(ruta)
    print(''.center(40, '-'))
    print(' CREAR TEMA '.center(40, '-'))
    print(' DESDE CERO '.center(40, '-'))
    sure = None
    while sure != '1':
        name = None
        while name is None:
            print(''.center(40, '-'))
            print(' Digite el nombre de su tema '.center(40, '-'))
            print(''.center(40, '-'))
            name = input()
            name = valid_pala_2(name)
            name = name.lower()
            name = name.capitalize()
            if name in dic_temas:
                print(''.center(40, '-'))
                print(' Su tema {} '.center(40).format(name))
                print(' Esta repetido '.center(40, '-'))
                print(' Por favor ingrese otro '.center(40, '-'))
                print(''.center(40, '-'))
            else:
                print(''.center(40, '-'))
                print(' Su tema es {} '.center(40).format(name))
                print(''.center(40, '-'))
                print(' Si esta seguro del nombre de su tema '.center(40, '-'))
                print(' digite 1 de lo contrario enter '.center(40, '-'))
                print(''.center(40, '-'))
                sure = input()
                sure = valid_selec(sure)
    print(''.center(40, '-'))
    print(' Digite el numero de palabras '.center(40, '-'))
    print(' a ingresar '.center(40, '-'))
    print(''.center(40, '-'))
    num = input()
    num = valid_num(num)
    palabras = list()
    for i in range(num):
        sure = None
        while sure != '1':
            print(''.center(40, '-'))
            print(' Digite su palabra '.center(40, '-'))
            print(''.center(40, '-'))
            palabra = input()
            palabra = valid_pala_2(palabra)
            while palabra in palabras:
                print(''.center(40, '-'))
                print(' Palabra repetida '.center(40, '-'))
                print(' digite otra'.center(40, '-'))
                print(''.center(40, '-'))
                palabra = input()
                palabra = valid_pala_2(palabra)
            print(''.center(40, '-'))
            print(' Su palabra es {} '.center(40).format(palabra))
            print(''.center(40, '-'))
            print(' Si esta seguro de su palabra '.center(40, '-'))
            print(' digite 1 de lo contrario enter '.center(40, '-'))
            print(''.center(40, '-'))
            sure = input()
            sure = valid_selec(sure)
            if sure == '1':
                palabra = palabra.lower()
                palabras.append(palabra)
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
    dicc = traer_temas(ruta)
    dicc[name] = palabras
    dicc = json.dumps(dicc, indent=3)
    archivo = open(ruta, 'w')
    archivo.write(dicc)
    archivo.close()
