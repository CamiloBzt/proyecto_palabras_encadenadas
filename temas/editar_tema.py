from temas.mostrar_temas import traer_temas
from procedimientos.validando import valid_num, valid_pala_2, valid_selec
import json


def add_pala(ruta: str) -> None:
    """
    Función que le permite al usuario agregar
    palabras a un tema.
    :param ruta: ruta del archivo de temas.
    """
    print(''.center(40, '-'))
    print(' AGREGAR'.center(40, '-'))
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
                    print(''.center(40, '-'))
                    print(' Digite el numero de palabras '.center(40, '-'))
                    print(' a agregar'.center(40, '-'))
                    print(''.center(40, '-'))
                    num = input()
                    num = valid_num(num)
                    # Ciclo para que el usuario ingrese
                    # el numero de palabras que digito.
                    for i in range(num):
                        sure = None
                        # Ciclo que va hasta que el usuario
                        # este seguro de su decisión.
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


def edit_pala(ruta: str) -> None:
    """
    Función que permite al usuario editar
    una palabra de cualquier tema.
    :param ruta: ruta del archivo de temas.
    """
    print(''.center(40, '-'))
    print(' EDITAR'.center(40, '-'))
    print(' PALABRA EXISTENTE '.center(40, '-'))
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
                    print(' Seleccione la palabra a editar '.center(40, '-'))
                    print(''.center(40, '-'))
                    print(' Digite 1 si la quiere elegir '.center(40, '-'))
                    print(' enter de lo contrario '.center(40, '-'))
                    print(''.center(40, '-'))
                    sure = None
                    while sure != '1':
                        word = None
                        # Ciclo que va hasta que el usuario
                        # escoja una palabra.
                        while not word:
                            for palabra in palabras:
                                if not word:
                                    print(''.center(40, '-'))
                                    print(palabra)
                                    print(''.center(40, '-'))
                                    selec = input()
                                    selec = valid_selec(selec)
                                    if selec == '1':
                                        word = palabra
                            if not word:
                                print(''.center(40, '-'))
                                print(' Por favor, seleccione una palabra '.center(40, '-'))
                                print(''.center(40, '-'))
                        print(''.center(40, '-'))
                        print(' Su palabra es {} '.center(40).format(word))
                        print(''.center(40, '-'))
                        print(''.center(40, '-'))
                        print(' Si esta seguro de su palabra '.center(40, '-'))
                        print(' digite 1 de lo contrario enter '.center(40, '-'))
                        print(''.center(40, '-'))
                        sure = input()
                        sure = valid_selec(sure)
                    sure = None
                    while sure != '1':
                        print('-'.center(40, '-'))
                        print(' Digite la palabra con '.center(40, '-'))
                        print(' los cambios a realizar '.center(40, '-'))
                        print('-'.center(40, '-'))
                        print(' Digite enter '.center(40, '-'))
                        print(' si no hay cambios '.center(40, '-'))
                        print(''.center(40, '-'))
                        new_pala = input('{}: '.format(word))
                        if new_pala == '':
                            sure = '1'
                        else:
                            new_pala = valid_pala_2(new_pala)
                            while new_pala in palabras:
                                print(''.center(40, '-'))
                                print(' Palabra repetida '.center(40, '-'))
                                print(' digite otra'.center(40, '-'))
                                print(''.center(40, '-'))
                                new_pala = input()
                                new_pala = valid_pala_2(new_pala)
                            print('-'.center(40, '-'))
                            print(' La palabra editada es {} '.center(40).format(new_pala))
                            print(' Si esta seguro de su palabra '.center(40, '-'))
                            print(' digite 1 de lo contrario enter '.center(40, '-'))
                            print(''.center(40, '-'))
                            sure = input()
                            sure = valid_selec(sure)
                            if sure == '1':
                                new_pala = new_pala.lower()
                                palabras.append(new_pala)
                                palabras.remove(word)
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


def remov_pala(ruta: str) -> None:
    """
    Función que permite al usuario borrar
    una palabra de cualquier tema.
    :param ruta: ruta del archivo de temas.
    """
    print(''.center(40, '-'))
    print(' BORRAR'.center(40, '-'))
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
                # Si el usuario escogió salir.
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
                    print(' Seleccione la palabra a borrar '.center(40, '-'))
                    print(''.center(40, '-'))
                    print(' Digite 1 si la quiere elegir '.center(40, '-'))
                    print(' enter de lo contrario '.center(40, '-'))
                    print(''.center(40, '-'))
                    for palabra in palabras:
                        print(''.center(40, '-'))
                        print(palabra)
                        print(''.center(40, '-'))
                        selec = input()
                        selec = valid_selec(selec)
                        if selec == '1':
                            palabras.remove(palabra)
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
