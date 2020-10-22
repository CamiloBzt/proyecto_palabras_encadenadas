from menus.principal import inicio, opcion, instrucciones, despedida
from menus.eleccion_dos import menu_dos, opciones_dos
from menus.eleccion_uno import jueguelo
from procedimientos.validando import valid_opcion, valid_menu_dos


def main() -> None:
    """
    Función principal.
    """
    inicio()
    ruta = "./temas_json/temas.json"
    eleccion = None
    while eleccion != "4":
        eleccion = opcion()
        if valid_opcion(eleccion):
            if eleccion == "1":
                jueguelo(ruta)
            elif eleccion == "2":
                opci = None
                while opci != "5":
                    opci = menu_dos()
                    if valid_menu_dos(opci):
                        opciones_dos(opci, ruta)
            elif eleccion == '3':
                instrucciones()

    despedida()


main()
