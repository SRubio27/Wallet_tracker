import api
import portfolio


def visualizar_wallet():
    
    opcion = int(input(
        """
        Que portfolio quieres visualizar?
            1.- Visualizacion general.
""" + "\n".join(["            {}.- Visualizar {}".format(i+2, wallet) for i, wallet in enumerate(opciones_portfolios)]) + """
        
        Opcion: """
    ))

    if opcion == 1:
        portfolio.visualizacion_general()

    if 1 < opcion <= len(opciones_portfolios) + 1:
        portfolio.visualizar_portfolio(opciones_portfolios[opcion-2])


opciones_portfolios = portfolio.obtener_portfolios()

def eliminar_valor():
    simbolo_crypto = "BTC"  # Cambia por el símbolo que quieras consultar
    print(api.obtener_precio_crypto(simbolo_crypto))

def obtener_precio():
    simbolo_crypto = input("Introduce el símbolo de la criptomoneda: ")
    return api.obtener_precio_crypto(simbolo_crypto)

def salir():
    print("Saliendo del programa...")
    exit()

def caso_default():
    return "Hubo un error inesperado, vuelva a intentarlo"

def anadir_valor():
    wallet = elegir_wallet()
    portfolio.anadir_valor(wallet)

def elegir_wallet():
    print("Portfolios disponibles:" + "\n".join(["\t{}.- {}".format(i+1, wallet) for i, wallet in enumerate(opciones_portfolios)]))
    wallet = int(input("Introduce el nombre del portfolio: "))
    return opciones_portfolios[wallet-1]



opciones = {
    1: visualizar_wallet,
    2: anadir_valor,
    3: eliminar_valor,
    4: obtener_precio,
    5: salir
}


if __name__ == "__main__":

    opcion = 0
    while opcion != 5:
        opcion = int(input(
            """
            Bienvenido al menú de gestión de portfolios, seleccione opción:
                1.- Visualizar portfolio/s.
                2.- Añadir nueva entrada.
                3.- Eliminar valor.
                4.- Consultar precio de una criptomoneda.
                5.- Salir.  

            Opcion: """
            ))

        resultado = opciones.get(opcion, caso_default)()
        if resultado:
            print(resultado)