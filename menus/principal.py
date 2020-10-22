def inicio() -> None:
    print("".center(40, "-"))
    print(" Bienvenido ".center(40, "-"))
    print(" a ".center(40, "-"))
    print(" Palabras Encadenadas ".center(40, "-"))
    print("".center(40, "-"))
    print("".center(40, "-"))


def opcion() -> str:
    print(" Seleccione una opción ".center(40, "-"))
    print("".center(40, "-"))
    print(" 1. Iniciar juego. ".center(40, "-"))
    print(" 2. Temas. ".center(40, "-"))
    print(' 3. Instrucciones. '.center(40, '-'))
    print(" 4. Salir del juego. ".center(40, "-"))
    print("".center(40, "-"))
    return input()


def despedida() -> None:
    print("-".center(40, "-"))
    print(" Gracias por jugar ".center(40, "-"))
    print(" Hasta la proxima ".center(40, "-"))
    print("-".center(40, "-"))


def instrucciones() -> None:
    print(''.center(105, '-'))
    print('El juego consiste en dar palabras encadenadas, en este caso la primera palabra será dada por el programa')
    print('y a partir de esta será el turno del primer jugador, quien deberá escribir una palabra cuya primera ')
    print('letra sea la última de la palabra dicha por el programa o jugador anterior, pero con una particularidad')
    print('la cual es que debe tener relación con el tema o uno de los temas que se haya/n escogido antes de iniciar')
    print('y así poco a poco ir formando una cadena de palabras. Por ejemplo: ')
    print('Tema: Instrumentos ')
    print('Palabra: Guitarra')
    print('Como esta termina en "a", el siguiente jugador tendrá ')
    print('que decir una palabra que empiece por "a", como: Acordeón ')
    print(''.center(105, '-'))
    print('El juego comienza pidiendo la cantidad de jugadores, y así mismo asignarle')
    print('un nombre a cada uno luego de esto podrás elegir uno o varios temas para iniciar el juego.')
    print(''.center(105, '-'))
    print('El jugador pierde si: ')
    print('La palabra dicha no cumple con la dinámica del juego')
    print('No tiene relación con el tema')
    print('Se repite una palabra antes dicha')
    print('El jugador en turno se rinde. ')
    print(''.center(65, '-'))
    print('El ganador y puntuación tendrá que ver con las vocales que ')
    print('valen un punto las consonantes que valen dos y la "ñ" vale cinco.')
    print(''.center(65, '-'))
    print(''.center(40, '-'))
