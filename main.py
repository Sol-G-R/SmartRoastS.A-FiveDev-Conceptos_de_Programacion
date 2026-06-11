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

    print("****************** PAÍS ******************")
    print("limpiado")
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
    print("limpiado")
    print("*********************************************\n")

    # ignorar Peso por ahora
    # print("****************** PESO ******************")
    # print("a decidir cómo usar")
    # print("*********************************************\n")

    print("****************** EMBALAJE ******************")
    print("limpiado")
    print("*********************************************\n")



#-----------------------------ESPACIO PARA FUNCIONES DE CÁLCULO------------------------------------
def sumar_tarifa_fija(estado,tarifa):
    resultado = 0
    return resultado

def calcular_flete(distancia,tarifa):
    resultado = 0
    return resultado

def calcular_total():
    # SOBRE costo_fin HAY QUE:
    #sumar costo_base
    #sumar resultado de sumar_tarifa_fija() con keys "eleccion_embalaje" y "embalaje"
    #sumar resultado de sumar_tarifa_fija() con keys "obligatorio_fitosanitario" y "fitosanitario"
    #sumar resultado de calcular_flete()

    #dividir costo_fin por iva y reasignarlo sobre sí mismo
    resultado = 0
    return resultado
#-----------------------------ESPACIO PARA FUNCIONES DE CÁLCULO------------------------------------



def imprimir_ticket():
    # ticket mostrando precio final, un desglose de cada costo, y los datos no-númericos (nombre, país)
    print()



# LO ÚNICO QUE EL PROGRAMA EJECUTA VERDADERAMENTE:
main()
precio_total = calcular_total()
imprimir_ticket(precio_total)