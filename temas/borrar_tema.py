from temas.mostrar_temas import traer_temas
from procedimientos.validando import valid_selec
import json


def elim_tema(ruta: str) -> None:
    """
    Función que permite al usuario eliminar un tema.
    :param ruta: ruta del archivo de temas.
    """
    print(''.center(40, '-'))
    print(' BORRAR TEMA'.center(40, '-'))
    print(''.center(40, '-'))
    print(' Seleccione el tema '.center(40, '-'))
    print(''.center(40, '-'))
    print(' Digite 1 si lo quiere borrar '.center(40, '-'))
    print(' enter de lo contrario '.center(40, '-'))
    print(''.center(40, '-'))
    # Diccionario de los temas (ver función traer_temas()).
    temas = traer_temas(ruta)
    tema = None
    for llave in temas:
        if not tema:
            print(''.center(40, '-'))
            print(llave.center(40))
            print(''.center(40, '-'))
            selec = input()
            selec = valid_selec(selec)
            if selec == '1' and selec != '':
                tema = llave
    if tema is not None:
        print(''.center(40, '-'))
        print('Esta seguro de eleminar'.center(40))
        print('el tema {}'.center(40).format(tema))
        print(''.center(40, '-'))
        print(' Digite 1 para confirmar '.center(40, '-'))
        print(' enter de lo contrario '.center(40, '-'))
        print(''.center(40, '-'))
        sure = input()
        if sure == '1':
            print(''.center(40, '-'))
            print(' El tema {} '.center(40).format(tema))
            print(' fue eliminado '.center(40))
            print(''.center(40, '-'))
            temas.pop(tema)
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
