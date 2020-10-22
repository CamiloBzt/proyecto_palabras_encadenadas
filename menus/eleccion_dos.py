from procedimientos.validando import valid_temas, valid_temas_2
from temas.agregar_tema import copiar_exist, create
from temas.consultar_tema import consul_pala, cant_pala, consul_pala_2
from temas.editar_tema import add_pala, edit_pala, remov_pala
from temas.borrar_tema import elim_tema


def menu_dos() -> str:
    print("-".center(40, "-"))
    print(" Selecione una opción ".center(40, "-"))
    print("-".center(40, "-"))
    print(" 1. Agregar un tema. ".center(40, "-"))
    print(" 2. Consultar un tema. ".center(40, "-"))
    print(" 3. Editar un tema. ".center(40, "-"))
    print(" 4. Borrar un tema. ".center(40, "-"))
    print(" 5. Volver. ".center(40, "-"))
    print("-".center(40, "-"))
    return input()


def opciones_dos(opcion: str, ruta: str) -> None:
    if opcion == "1":
        elec = None
        while elec != "3":
            print(" AGREGAR UN TEMA ".center(40, "-"))
            print("-".center(40, "-"))
            print(" Selecione una opción ".center(40, "-"))
            print("-".center(40, "-"))
            print(" 1. Copiar de tema existente ".center(40, "-"))
            print(" y agregar palabras. ".center(40, "-"))
            print(" 2. Crear desde ceros. ".center(40, "-"))
            print(" 3. Volver. ".center(40, "-"))
            print("-".center(40, "-"))
            elec = input()
            if not valid_temas(elec):
                elec = None
            if elec == '1':
                copiar_exist(ruta)
            elif elec == '2':
                create(ruta)
    elif opcion == "2":
        elec = None
        while elec != "4":
            print(" CONSULTAR UN TEMA ".center(40, "-"))
            print("-".center(40, "-"))
            print(" Selecione una opción ".center(40, "-"))
            print("-".center(40, "-"))
            print(" 1. Consultar palabras. ".center(40, "-"))
            print(" 2. Consultar si palabra existe. ".center(40, "-"))
            print(" 3. Consultar cantidad de palabras. ".center(40, "-"))
            print(" 4. Volver. ".center(40, "-"))
            print("-".center(40, "-"))
            elec = input()
            if not valid_temas_2(elec):
                elec = None
            if elec == '1':
                consul_pala(ruta)
            elif elec == '2':
                consul_pala_2(ruta)
            elif elec == '3':
                cant_pala(ruta)
    elif opcion == "3":
        elec = None
        while elec != "4":
            print(" EDITAR UN TEMA ".center(40, "-"))
            print("-".center(40, "-"))
            print(" Selecione una opción ".center(40, "-"))
            print("-".center(40, "-"))
            print(" 1. Agregar palabras. ".center(40, "-"))
            print(" 2. Editar palabra existente. ".center(40, "-"))
            print(" 3. Borrar palabras. ".center(40, "-"))
            print(" 4. Volver. ".center(40, "-"))
            print("-".center(40, "-"))
            elec = input()
            if not valid_temas_2(elec):
                elec = None
            if elec == '1':
                add_pala(ruta)
            elif elec == '2':
                edit_pala(ruta)
            elif elec == '3':
                remov_pala(ruta)
    elif opcion == "4":
        elim_tema(ruta)
