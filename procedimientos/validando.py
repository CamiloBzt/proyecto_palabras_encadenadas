def valid_opcion(opci: str) -> bool:
    valid = ["1", "2", "3", '4']
    if opci in valid:
        return True
    else:
        print("-".center(40, "-"))
        print(" Selecione una opción valida ".center(40, "-"))
        print("-".center(40, "-"))
        return False


def valid_menu_dos(opcion: str) -> bool:
    valid = ["1", "2", "3", "4", "5"]
    if opcion in valid:
        return True
    else:
        print("-".center(40, "-"))
        print(" Selecione una opción valida ".center(40, "-"))
        print("-".center(40, "-"))
        return False


def valid_temas(opcion: str) -> bool:
    valid = ["1", "2", "3"]
    if opcion in valid:
        return True
    else:
        print("-".center(40, "-"))
        print(" Selecione una opción valida ".center(40, "-"))
        print("-".center(40, "-"))
        return False


def valid_temas_2(opcion: str) -> bool:
    valid = ["1", "2", "3", '4']
    if opcion in valid:
        return True
    else:
        print("-".center(40, "-"))
        print(" Selecione una opción valida ".center(40, "-"))
        print("-".center(40, "-"))
        return False


def valid_selec(selec: str) -> str:
    while selec != '1' and selec != '':
        print('-'.center(40, '-'))
        print(' Digite una opción valida '.center(40, '-'))
        print('-'.center(40, '-'))
        selec = input()
    return selec


def valid_jugadores(juga: str) -> bool:
    num = ['1', "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if juga in num:
        return True
    else:
        print("-".center(40, "-"))
        print(" Por favor digite un numero entero valido ".center(40, "-"))
        print("-".center(40, "-"))
        return False


def valid_num(num: str) -> int:
    while not num.isnumeric():
        print("-".center(40, "-"))
        print(" Digite un numero entero ".center(40, "-"))
        print("-".center(40, "-"))
        num = input()
    num = int(num)
    return num


def valid_pala(palabra: str) -> str:
    if palabra != '':
        valid = False
        while not valid:
            if not palabra.isalpha():
                valid = False
                print("-".center(40, "-"))
                print(" Por favor, digite bien su palabra ".center(40, "-"))
                print("-".center(40, "-"))
                palabra = input()
            else:
                valid = True
    return palabra


def valid_pala_2(palabra: str) -> str:
    valid = False
    while not valid:
        if not palabra.isalpha():
            valid = False
            print("-".center(40, "-"))
            print(" Por favor, digite bien su palabra ".center(40, "-"))
            print("-".center(40, "-"))
            palabra = input()
        else:
            valid = True
    return palabra
