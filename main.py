# Diccionario de variables del ticket (todas las variables que se registren acá van a mostrarse)
dicc = {
    "nombre": "x",
    "costo_base": 0.0,
    "pais": ["Bolivia", "Paraguay", "Uruguay"],
    "region": ["Norte", "Sur", "-"],
    "transporte": ["Terrestre ($0.5/km)", "Aéreo ($0.8/km)"],
    "peso": 0,
    "embalaje": False,
    "fitosanitario": 150,
    "iva": ["15%", "10%", "22%"],
    "costo_fin": 0.0
}

def aniadir_a_dicc(key):
    valor = input("usuario ingresa el valor del key: ")
    dicc[key] = valor

# [explicación]
"""
aniadir_a_dicc("nombre",x)
"""

# NOTA: ya que tenemos el diccionario de referencia, acordemos que los nombres de todas las variables tengan un máximo de 2 palabras y lo más abreviadas posible (EJ: color, altura_base, cant_max) para mayor agilidad, pero siempre manteniéndose entendibles

# Recuerden mantener buena ortografía y espaciado en los textos que se muestran al usuario
print("\n---------------------------------------------------------------------")
print("    ¡Bienvenido al cotizador de exportación de SmartRoast S.A.!\nIntroduzca la información de su pedido y se le devolverá la cantidad\nexacta que pagaría por el total de la operación, incluyendo costos\nde aduana e impuestos.")
print("---------------------------------------------------------------------\n")

print("****************** NOMBRE ******************")
input(print("Ingrese el nombre de la persona a cargo del pedido: "))
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