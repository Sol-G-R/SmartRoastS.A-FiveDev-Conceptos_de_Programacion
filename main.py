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
    "fitosanitario": 150,
    "obligatorio_fitosanitario": True
}

venta = {
    #"nombre": "x",
    #"costo_base": 0.0,
    #"pais": "x",
    #"dist_region": 0 (referir a dicc),
    #"tarifa_transporte": 0 (referir a dicc),
    #"peso": 0,
    #"eleccion_embalaje": True,
    #"iva": 0 (referir a dicc),
    #"costo_fin": 0.0
}



def main():
    print("\n" + "-"*70)
    print(" "*4 + "¡Bienvenido al cotizador de exportación de SmartRoast S.A.!\nIntroduzca la información de su pedido y se le devolverá la cantidad\nexacta que pagaría por el total de la operación, incluyendo costos\nde transporte, IVA y otros recargos.")
    print("-"*70 + "\n")


    print(f" NOMBRE ".center(85, "*"))
    print("limpiado")
    print("*"*85 + "\n")


    print(f" COSTO BASE ".center(85, "*"))
# siguiendo los datos del sitio web se establecen los costos máximos y mínimos
    while True:
        try:
            costo = float(input("Ingrese el costo base del pedido: "))
            if costo >= 12000 and costo <= 172500000:
                venta["costo_base"] = costo
                break
            elif costo > 172500000:
                print("  --> [ERROR] El costo excede el límite esperado, verifique el valor de su compra.\n")
            else:
                print("  --> [ERROR] El costo mínimo de un paquete es $12,000.\n")
        except ValueError:
            print("  --> [ERROR] Ingrese solo un número.\n")
    
    print(f"  --> Costo base registrado: ${venta['costo_base']:.2f}")
    print("*"*85 + "\n")


    print(f" PAÍS ".center(85, "*"))
    paises = []
    for clave, valor in dicc.items():
        if isinstance(valor, dict):
            paises.append(clave)
    while True:
        try:
            print("Países de destino:")

            for i, pais in enumerate(paises, start=1):
                print(f"{i} - {pais.capitalize()}")

            opcion = int(input("Seleccione un país: "))

            if 1 <= opcion <= len(paises):
                venta["pais"] = paises[opcion - 1]
                break

            print("  --> [ERROR] No es una de las opciones disponibles.\n")
        except ValueError:
            print("  --> [ERROR] Ingrese solo un número.\n")

    venta["iva"] = dicc[venta['pais']]["iva"]
    print(f"  --> País seleccionado: {venta['pais'].capitalize()}")
    print("*"*85 + "\n")


    print(f" REGIÓN ".center(85, "*"))
    match venta["pais"]:
        case "bolivia":
            while True:
                region = input("Ingrese la región de destino (norte/sur): ").strip().lower()
                if region == "norte":
                    venta["dist_region"] = dicc["bolivia"]["norte"]
                    break
                elif region == "sur":
                    venta["dist_region"] = dicc["bolivia"]["sur"]
                    break
                else:
                    print("  --> [ERROR] No es una de las opciones disponibles.\n")
        case "paraguay":
            while True:
                region = input("Ingrese la región (norte/sur): ").strip().lower()
                if region == "norte":
                    venta["dist_region"] = dicc["paraguay"]["norte"]
                    break
                elif region == "sur":
                    venta["dist_region"] = dicc["paraguay"]["sur"]
                    break
                else:
                    print("  --> [ERROR] No es una de las opciones disponibles.\n")
        case "uruguay":
            print("Este país posee una única región de envío.")
            venta["dist_region"] = dicc["uruguay"]["unica"]

    print(f"  --> Distancia del envío: {venta['dist_region']}km")
    print("*"*85 + "\n")


    print(f" TRANSPORTE ".center(85, "*"))
    while True:
        opcion = input("Seleccione el tipo de transporte (terrestre/aereo): ").strip().lower()

        if opcion in ["terrestre", "aereo"]:
            venta["tarifa_transporte"] = dicc[opcion]
            break
        else:
            print("  --> [ERROR] Opción inválida. Escriba 'terrestre' o 'aereo'.")

    print(f"  --> Tarifa del tipo de transporte: ${venta["tarifa_transporte"]}/km")
    print("*"*85 + "\n")


    print(f" PESO ".center(85, "*"))
# siguiendo los datos del sitio web se establece el peso máximo y mínimo
    while True:
        try: 
            kilos = int(input("Ingrese el peso del pedido en kilogramos: "))
            if kilos >= 1 and kilos <= 15000:
                venta["peso"] = kilos
                break
            elif kilos > 15000:
                print("  --> [ERROR] El peso excede el límite esperado, verifique el volumen de su compra.\n")
            else:
                print("  --> [ERROR] El peso mínimo de un pedido es 1kg.\n")
        except ValueError:
            print("  --> [ERROR] Ingrese solo un número.\n")
    
    print(f"  --> Peso del pedido registrado: {venta["peso"]}kg")
    print("*"*85 + "\n")


    print(f" EMBALAJE ".center(85, "*"))
    while True:
        embalaje = input("¿Desea que su pedido cuente con Embalaje Especial e Higroscópico? (si/no): ").strip().lower()

        if embalaje == "si":
            print("  --> Se agregó Embalaje Especial e Higroscópico al pedido.")
            venta["eleccion_embalaje"] = True
            break
        elif embalaje == "no":
            print("  --> El pedido se enviará sin Embalaje Especial e Higroscópico.")
            venta["eleccion_embalaje"] = False
            break
        else:
            print("  --> [ERROR] Opción inválida. Escriba únicamente 'si' o 'no'.")
    print("*"*85 + "\n")



#-----------------------------ESPACIO PARA FUNCIONES DE CÁLCULO------------------------------------
def sumar_tarifa_fija(estado,tarifa):
    if estado == True:
        return tarifa
    else:
        return 0

def calcular_flete(distancia,tarifa):
    resultado = distancia * tarifa
    return resultado

def calcular_recargo_peso(kilos):
    if kilos > 1000 and kilos <= 10000:
        resultado = 50000
    elif kilos > 10000:
        resultado = 500000
    else:
        resultado = 0
    return resultado

def calcular_total():
    costo_fin = 0.0

    costo_fin += venta["costo_base"]

    costo_fin += sumar_tarifa_fija(
        venta["eleccion_embalaje"],
        dicc["embalaje"]
    )

    costo_fin += sumar_tarifa_fija(
        dicc["obligatorio_fitosanitario"],
        dicc["fitosanitario"]
    )

    costo_fin += calcular_flete(
        venta["dist_region"],
        venta["tarifa_transporte"]
    )

    costo_fin += calcular_recargo_peso(venta["peso"])

    costo_fin += costo_fin * (venta["iva"] / 100)

    return round(costo_fin, 2)
#-----------------------------ESPACIO PARA FUNCIONES DE CÁLCULO------------------------------------

def imprimir_ticket():
    # ticket mostrando costo_fin, un desglose de cada costo, y los datos no-númericos (nombre, país, región, etc.)
    print()



# LO ÚNICO QUE EL PROGRAMA EJECUTA VERDADERAMENTE:
main()
costo_fin = calcular_total()
imprimir_ticket()