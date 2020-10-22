import json


def traer_temas(ruta: str) -> dict:
    """
    Función que retorna un diccionario con los temas y palabras.
    :param ruta: ruta del archivo de temas.
    :return: diccionario de temas.
    """
    archivo = open(ruta, 'r')
    dic_temas = json.loads(archivo.read())
    archivo.close()
    return dic_temas


def save_temas(ruta: str, temas: list, palabra: str) -> None:
    """
    Función que guarda las palabras que se validen
    durante una partida.
    :param ruta: ruta del archivo de temas.
    :param temas: temas escogidos en la partida.
    :param palabra: palabra digitada por el jugador.
    """
    temas_dic = traer_temas(ruta)
    if len(temas) == 1:
        palabras = temas_dic.get(temas[0])
        palabras.append(palabra)
        temas_dic[temas[0]] = palabras
        temas_dic = json.dumps(temas_dic, indent=3)
        archivo = open(ruta, "w")
        archivo.write(temas_dic)
        archivo.close()
    else:
        print(''.center(40, '-'))
        print(' Digite a que tema pertenece '.center(40, '-'))
        print(' la palabra {} '.center(40).format(palabra))
        print(''.center(40, '-'))
        topic = None
        while not topic:
            for tema in temas:
                if not topic:
                    print(' Digite 1 si es del tema'.center(40, '-'))
                    print(' enter de lo contrario '.center(40, '-'))
                    print(''.center(40, '-'))
                    print(tema.center(40))
                    print(''.center(40, '-'))
                    selec = input()
                    while selec != '1' and selec != '':
                        print('-'.center(40, '-'))
                        print(' Digite una opción valida '.center(40, '-'))
                        print('-'.center(40, '-'))
                        selec = input()
                    if selec == '1' and selec != '':
                        topic = tema
        palabras = temas_dic.get(topic)
        palabras.append(palabra)
        temas_dic[topic] = palabras
        temas_dic = json.dumps(temas_dic, indent=3)
        archivo = open(ruta, "w")
        archivo.write(temas_dic)
        archivo.close()
        print(''.center(40, '-'))
        print(' Gracias '.center(40, '-'))
        print(' Volvamos al juego '.center(40, '-'))
        print(''.center(40, '-'))
