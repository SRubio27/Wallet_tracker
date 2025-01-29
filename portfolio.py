import os

import api


def obtener_portfolios():
    portfolios = []
    
    for file in os.listdir("./docs"): 
        file_str = str(file).replace(".csv", "")   
        portfolios.append(file_str)
    return portfolios

def visualizacion_general():
    portfolios = obtener_portfolios()
    for wallet in portfolios:
        with open("./docs/{}.csv".format(wallet), "r") as portfolio:
            continue




def visualizar_portfolio(wallet):
    with open("./docs/{}.csv".format(wallet), "r") as portfolio:
        valor_total = 0
        invertido_total = 0
        print(f"{'Símbolo':<10} {'Unidades':<15} {'Valor':<15} {'Invertido':<15} {'Rentabilidad':<15}")
        print("-" * 70)
        for line in portfolio:
            line = line.strip().split(",")

            simbolo = line[0].upper()
            precio_str = api.obtener_precio_crypto(simbolo)
            try:
                precio = float(precio_str)
            except ValueError:
                print(f"Error al obtener el precio para el símbolo: {simbolo}")
                continue

            valor = precio * float(line[1])
            valor_total += valor
            rentabilidad = valor - float(line[2])
            invertido_total += float(line[2])
            print(f"{simbolo:<10} {line[1]:<15} ${valor:<14.2f} ${float(line[2]):<14.2f} ${rentabilidad:<14.2f}")
        
        print("-" * 70)
        print(f"{'Total actual:':<25} ${valor_total:.2f}")
        print(f"{'Total invertido:':<25} ${invertido_total:.2f}")
        print(f"{'Rentabilidad total:':<25} ${valor_total - invertido_total:.2f}")
        print("-" * 70)

    
def simbolo_ya_anadido(simbolo, wallet):
    with open("./docs/{}.csv".format(wallet), "r") as portfolio:
        for line in portfolio:
            if line.strip().split(",")[0].upper() == simbolo.upper():
                return True, line.strip().split(",")
    return False, None

def anadir_valor(wallet):
    portfolio = open("./docs/{}.csv".format(wallet), "a")
    simbolo = input("Introduce el símbolo de la criptomoneda: ")

    if not api.obtener_precio_crypto(simbolo):
        return  "Símbolo no encontrado."

    cantidad_str = input("Introduce la cantidad de unidades: ").replace(',', '.')
    invertido_str = input("Introduce la cantidad invertida: ").replace(',', '.')

    cantidad = float(cantidad_str)
    invertido = float(invertido_str)
    
    encontrado, linea = simbolo_ya_anadido(simbolo, wallet)    
    if not encontrado:
        
        print(f"{simbolo}: {cantidad} unidades, invertido: ${invertido:.2f}") 

        if input("¿Es correcto? (y/n): ") == "y":
            portfolio.write(f"{simbolo.upper()},{cantidad},{invertido}\n")
            portfolio.close()
            print("Entrada añadida correctamente.")
        else:
            print("Entrada cancelada.")
            portfolio.close()

    else: 
        linea[1] = str(float(linea[1]) + cantidad)
        linea[2] = str(float(linea[2]) + invertido)

        with open("./docs/{}.csv".format(wallet), "r") as portfolio:
            lines = portfolio.readlines()
        with open("./docs/{}.csv".format(wallet), "w") as portfolio:
            for line in lines:
                if line.strip().split(",")[0].upper() == simbolo.upper():
                    portfolio.write(",".join(linea) + "\n")
                else:
                    portfolio.write(line)
        print("Entrada actualizada correctamente.")