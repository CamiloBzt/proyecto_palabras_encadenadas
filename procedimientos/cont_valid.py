def contador(palabra: str) -> int:
    """
    Función que retorna los puntos obtenidos por la palabra digitada.
    :param palabra: palabra digitada por el jugador.
    :return: retorna puntaje obtenido por palabra.
    """
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                   'z''B', 'C', 'D',
                   'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    cont = 0
    for letra in palabra:
        if letra in vocales:
            cont += 1
        elif letra in consonantes:
            cont += 2
        elif letra == 'ñ':
            cont += 5
    return cont


def valid_word(word_1: str, word_2: str) -> bool:
    """
    Función que valida si la palabra sigue la dinamica del juego.
    :param word_1: palabra anterior.
    :param word_2: palabra a evaluar.
    :return: retorna si la palabra es valida o no.
    """
    primera = word_2[0]
    ultima = word_1[len(word_1) - 1]
    if primera == ultima:
        return True
    else:
        return False


def ganador(jugadores: dict, elimina: list) -> None:
    """
    Función que retorna el ganador de la partida.
    :param jugadores: diccionario con los nombre y
                     puntajes de cada jugador.
    :param elimina: lista con los jugadores eliminados.
    """
    cont = 0
    for jugador in jugadores:
        cont += jugadores[jugador]
    if cont == 0:
        for jugador in jugadores:
            if jugador not in elimina:
                print(''.center(40, '-'))
                print(' El ganador es: '.center(40, '-'))
                print(' El jugador {} con {} puntos. '.center(40).format(jugador, jugadores[jugador]))
                print(''.center(40, '-'))
    else:
        name = None
        punt = 0
        for nom, puntos in jugadores.items():
            punt_1 = puntos
            if punt_1 > punt:
                name = nom
                punt = punt_1
        print(''.center(40, '-'))
        print(' El ganador es: '.center(40, '-'))
        print(' El jugador {} con {} puntos. '.center(40).format(name, punt))
        print(''.center(40, '-'))
