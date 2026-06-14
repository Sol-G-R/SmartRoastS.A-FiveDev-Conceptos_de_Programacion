# Diccionarios de variables del ticket (solo las que podrían llegar a mostrarse en el ticket final)
dicc = {
    "bolivia": {
        "norte": 2010, 
        "sur": 1300,

        "iva": 15
    },
    "paraguay": {
        "norte": 1534, 
        "sur"  : 1235,

        "iva": 10
    },
    "uruguay": {
        "unica": 995,

        "iva": 22
    },

    "terrestre": 0.5,
    "aereo": 0.8,

    "embalaje": 450,
    "fitosanitario": 150
}

venta = {
    #"nombre": "x",
    #"costo_base": 0.0,
    #"pais": "x",
    #"region": "referir a dicc",
    #"costo_region": 0.0,
    #"transporte": "referir a dicc",
    #"peso": 0,
    #"eleccion_embalaje": True,
    #"obligatorio_fitosanitario": True,
    #"iva": "referir a dicc",
    #"costo_fin": 0.0
}
# Las entradas de "venta" serán creadas en la sección que corresponda con los inputs del usuario.
# Si es un key totalmente nuevo, irá, por ejemplo:
#       venta[peso] = int(input("usuario, ingrese el peso del paquete: "))
# Si es un key basado en un valor NUMÉRICO fijo del "dicc", irá, por ejemplo:
#       venta[iva] = dicc[paraguay][iva]



#               El profe dijo que el menú debería ir dentro de su propia función, el "main"
def main():
    # Recuerden mantener buena ortografía y espaciado en los textos que se muestran al usuario
    print("\n" + "-"*69)
    print(" "*4 + "¡Bienvenido al cotizador de exportación de SmartRoast S.A.!\nIntroduzca la información de su pedido y se le devolverá la cantidad\nexacta que pagaría por el total de la operación, incluyendo costos\nde transporte, IVA y otros recargos.")
    print("-"*69 + "\n")

    print("****************** NOMBRE ******************")
    print("limpiado")
    print("*********************************************\n")

    print("****************** COSTO BASE ******************")
    print("limpiado")
    print("*********************************************\n")
    while True:
        try:
            costo = float(input("Ingrese el costo base del pedido en dólares: "))
            if costo > 0:
                venta["costo_base"] = costo
                print(f"Costo base registrado: ${costo:.2f}")
                break
            else:
                print("[ERROR] El costo debe ser un número positivo.")
        except ValueError:
            print("[ERROR] Por favor, ingrese un número válido.")

    print("****************** PAÍS ******************")
    #print("limpiado")
    seleccionar_pais()
    print(f"País seleccionado: {venta['pais'].capitalize()}\n")
    print("*********************************************\n")

    print("****************** REGIÓN ******************")
    match venta["pais"]:
        case "bolivia":
            region = input("Ingrese región (norte/sur): ").strip().lower()
            if region == "sur":
                venta["region"] = dicc["bolivia"]["sur"]
            else:
                venta["region"] = dicc["bolivia"]["norte"]
        case "paraguay":
            region = input("Ingrese región (norte/sur): ").strip().lower()
            if region == "sur":
                venta["region"] = dicc["paraguay"]["sur"]
            else:
                venta["region"] = dicc["paraguay"]["norte"]
        case "uruguay":
            venta["region"] = "unica"
            venta["costo_region"] = dicc["uruguay"]["unica"]
    print("*********************************************\n")

    print("****************** TRANSPORTE ******************")
while True:
    opcion = input("Ingrese el tipo de transporte ('terrestre' o 'aereo'): ").strip().lower()

    if opcion in ["terrestre", "aereo"]:
        venta["transporte"] = dicc[opcion]
        print(f"Transporte seleccionado exitosamente: {opcion.capitalize()}")
        break

    else:
        print("[ERROR] Opción inválida. Por favor, escriba 'terrestre' o 'aereo'.")
    print("*********************************************\n")

    # ignorar Peso por ahora
    # print("****************** PESO ******************")
    # print("a decidir cómo usar")
    # print("*********************************************\n")

    #A chequear, lo hice así y dsps confirmamos como lo vamos a hacer
    print("******************** PESO ********************")
    venta["peso"] = float(input("Ingrese el peso del pedido en kilogramos: "))
    print("**********************************************\n")

    print("****************** EMBALAJE ******************")
    print("limpiado")
    print("*********************************************\n")



#-----------------------------ESPACIO PARA FUNCIONES DE CÁLCULO------------------------------------
def sumar_tarifa_fija(estado,tarifa):
    if estado:
        return tarifa
    return 0

def calcular_flete(distancia,tarifa):
    resultado = distancia * tarifa
    return resultado

def calcular_total():
    costo_fin = 0.0

    # costo base
    costo_fin += venta["costo_base"]

    # embalaje
    costo_fin += sumar_tarifa_fija(
        venta["eleccion_embalaje"],
        dicc["embalaje"]
    )

    # certificado fitosanitario
    costo_fin += sumar_tarifa_fija(
        venta["obligatorio_fitosanitario"],
        dicc["fitosanitario"]
    )

    # flete
    costo_fin += calcular_flete(
        venta["peso"],
        venta["transporte"]
    )

    # IVA
    costo_fin += costo_fin * (venta["iva"] / 100)

    return round(costo_fin, 2)
#-----------------------------ESPACIO PARA FUNCIONES DE CÁLCULO------------------------------------

#Función que selecciona al país de destino.
def seleccionar_pais():

    paises = []

    for clave, valor in dicc.items():
        if isinstance(valor, dict):
            paises.append(clave)

    while True:

        try:
            print("\nSeleccione el país de destino:")

            for i, pais in enumerate(paises, start=1):
                print(f"{i} - {pais.capitalize()}")

            opcion = int(input("Seleccione un país: "))

            if 1 <= opcion <= len(paises):
                venta["pais"] = paises[opcion - 1]
                return

            print("Opción inválida.")

        except ValueError:
            print("Debe ingresar un número.")

def imprimir_ticket():
    # ticket mostrando precio final, un desglose de cada costo, y los datos no-númericos (nombre, país)
    print()



# LO ÚNICO QUE EL PROGRAMA EJECUTA VERDADERAMENTE:
main()
precio_total = calcular_total()
imprimir_ticket()



# Solicitar decisión del cliente

while True:
    embalaje = input(
        "¿Desea Embalaje Especial e Higroscópico? (si/no): "
    ).strip().lower()

    if embalaje == "si":
        print("Se agregó Embalaje Especial e Higroscópico al pedido.")
        break

    elif embalaje == "no":
        print("Pedido sin Embalaje Especial e Higroscópico.")
        break

    else:
        print("Opción inválida. Ingrese únicamente 'si' o 'no'.")




# Solicitar el peso del pedido en kilogramos

peso = float(input("Ingrese el peso del pedido en kilogramos: "))

print("El peso ingresado es:", peso, "kg")
