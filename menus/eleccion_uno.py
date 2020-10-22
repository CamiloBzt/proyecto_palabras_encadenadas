import random
from procedimientos.validando import valid_jugadores, valid_pala, valid_selec
from temas.mostrar_temas import traer_temas, save_temas
from procedimientos.cont_valid import contador, valid_word, ganador


def jueguelo(ruta: str) -> None:
    """
    Función que ejecuta el juego.
    :param ruta: ruta del archivo de los temas.
    """
    palabras = list()
    tem_list = list()
    print("".center(40, "-"))
    print(" Digite la cantidad de jugadores ".center(40, "-"))
    print(" Maximo 10 jugadores ".center(40, "-"))
    print("".center(40, "-"))
    num_juga = input()
    while not valid_jugadores(num_juga):
        num_juga = input()
    num_juga = int(num_juga)
    jugadores = dict()
    # Ciclo para agregar los nombres de los jugadores por partida.
    for jugador in range(1, num_juga + 1):
        mensaje = " Digite el nombre del jugador #{num}".format(num=str(jugador))
        print("".center(40, "-"))
        print(mensaje.center(40, "-"))
        print("".center(40, "-"))
        name = input()
        while name in jugadores:
            print("".center(40, "-"))
            print(" Nombre ya ingresado ".center(40, "-"))
            print("".center(40, "-"))
            name = input()
        jugadores[name] = 0
    print(' Los jugadores son: '.center(40, '-'))
    for llave in jugadores:
        print(llave)
    # Ciclo para agregar las palabras que se jugaran en la partida.
    while not palabras:
        print(' Seleccione los temas a jugar: '.center(40, '-'))
        print(' Digite 1 si lo quiere elegir '.center(40, '-'))
        print(' enter de lo contrario '.center(40, '-'))
        print('-'.center(40, '-'))
        temas = traer_temas(ruta)
        # Ciclo que muestra al usuario todos los temas.
        for llave in temas:
            print('-'.center(40, '-'))
            print(llave)
            print('-'.center(40, '-'))
            selec = input()
            selec = valid_selec(selec)
            if selec == '1' and selec != '':
                tem_list.append(llave)
                palabras = temas.get(llave) + palabras
        # Si el usurio no ingreso ningun tema puede salir a inicio.
        if not palabras:
            print(' Si quiere salir '.center(40, '-'))
            print(' Digite enter de lo contrario 1'.center(40, '-'))
            print('-'.center(40, '-'))
            salir = input()
            salir = valid_selec(salir)
            if salir == '':
                from app import main
                exit(main)

    word = random.choice(palabras)
    lista_jug = list()
    for llave in jugadores:
        lista_jug.append(llave)
    elimina = list()
    repetidos = list()
    jug = len(lista_jug)
    # Condición para juego de mas de un jugador
    if len(lista_jug) != 1:
        jug = len(lista_jug) - 1
    # Ciclo: hasta que solo quede un jugador se acabe el juego.
    while len(elimina) != jug:
        for jugador in lista_jug:
            # Condición que funciona para que no me repita el jugador si el juego ya acabo.
            if not (len(elimina) == jug):
                # Condición para que no se juegue mas con los jugadores eliminados.
                if not (jugador in elimina):
                    print(''.center(40, '-'))
                    print(' La palabra es: '.center(40, '-'))
                    print(''.center(40, '-'))
                    print(' {} '.format(word).center(40))
                    valid = True
                    print(''.center(40, '-'))
                    print('Digite su palabra jugador {} '.format(jugador).center(40))
                    print(' Si se rinde presione enter '.center(40, '-'))
                    print(''.center(40, '-'))
                    word_2 = input()
                    word_2 = valid_pala(word_2)
                    word_2 = word_2.lower()
                    print(''.center(40, '-'))
                    if not (word_2 == '') and not (word_2 in palabras):
                        # Condiciones que validan la palabra.
                        if not (valid_word(word, word_2)):
                            valid = False
                        if word_2 in repetidos:
                            valid = False
                        if not (word_2 in repetidos) and valid == True:
                            print(''.center(40, '-'))
                            print(' Digite 1, si {} es valida '.format(word_2).center(40))
                            print(' De lo contrario presione enter '.center(40, '-'))
                            print(''.center(40, '-'))
                            valida = input()
                            valida = valid_selec(valida)
                            if valida == '':
                                valid = False
                            elif valida == '1':
                                save_temas(ruta, tem_list, word_2)
                    elif word_2 == '':
                        valid = False
                    # Si la palabra siguió la dinamica.
                    if valid:
                        repetidos.append(word_2)
                        word = word_2
                        jugadores[jugador] += contador(word_2)
                    # Si la palabra no sigió la dinamica.
                    else:
                        print(''.center(40, '-'))
                        print(' Jugador {} fue eliminado '.center(40).format(jugador))
                        print(''.center(40, '-'))
                        elimina.append(jugador)
    print(''.center(40, '-'))
    print(' Los puntajes del juego fueron: '.center(40, '-'))
    print(''.center(40, '-'))
    for jug, punt in jugadores.items():
        print(jug, punt)
    ganador(jugadores, elimina)
