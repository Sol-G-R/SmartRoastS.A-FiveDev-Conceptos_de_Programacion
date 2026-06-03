# Diccionario de variables del ticket (todas las variables del programa se registran aca)
dicc = {
    "pais": {
        "bolivia": {
            "region": {"norte": "x", "sur": "x"},
            "iva": 15
        },

        "paraguay": {
            "region": {"norte": "x", "sur": "x"},
            "iva": 10
        },
        
        "uruguay": {
            "region": {"unica": "x"},
            "iva": 22
        },
    },

    "ninguno": {
        "ninguno": {
            "transporte": {"terrestre": 0.5, "aereo": 0.8},

            "ninguno": {
                "nombre": "x",
                "costo_base": 0.0,
                "peso": 0,
                "embalaje": False,
                # "fitosanitario": 150,
                "costo_fin": 0.0
            }
        }
    }
}


def aniadir_a_dicc(subdicc1, subdicc2, subdicc3, key, valor):
    dicc[subdicc1][subdicc2][subdicc3][key] = valor

# DENTRO DE CADA SECCIÓN HABRÁN LAS SIGUIENTES ASIGNACIONES:
# subdicc1 = "nombre de primer subdiccionario (o "ninguno" de no tener)"
# subdicc2 = "nombre de segundo subdiccionario (o "ninguno" de no tener)"
# subdicc3 = "nombre de tercer subdiccionario (o "ninguno" de no tener)"
# key = "key de la sección"
# valor = input("usuario ingresa el valor del key: ")
# MÁS EL LLAMADO A LA FUNCIÓN ANTERIOR

# Recuerden mantener buena ortografía y espaciado en los textos que se muestran al usuario
print("\n---------------------------------------------------------------------")
print("    ¡Bienvenido al cotizador de exportación de SmartRoast S.A.!\nIntroduzca la información de su pedido y se le devolverá la cantidad\nexacta que pagaría por el total de la operación, incluyendo costos\nde aduana e impuestos.")
print("---------------------------------------------------------------------\n")

print("****************** NOMBRE ******************")
input("limpiado")
print("*********************************************\n")

print("****************** COSTO BASE ******************")
print("limpiado")
print("*********************************************\n")

print("****************** PAÍS ******************")
print("limpiado")
print("*********************************************\n")

print("****************** REGIÓN ******************")
print("limpiado")
print("*********************************************\n")

print("****************** TRANSPORTE ******************")
print("limpiado")
print("*********************************************\n")

print("****************** PESO ******************")
print("limpiado")
print("*********************************************\n")



# Ticket
print("el total es ...")
print("---------------------------------------------------------------------")