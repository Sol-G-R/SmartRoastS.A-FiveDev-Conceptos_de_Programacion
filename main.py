# Diccionario de variables (TODAS las variables que usen deben registrarse acá, con sus tipos y propósitos)

precio_fin = 0 #FLOAT. Cantidad de plata que se le mostrará al cliente en el ticket (variable acumuladora que se pasa de sección a sección)
uno_pais = 0 #STR. País destinatario del envío (variable nacida de sección 1)
uno_prodep = 0 #STR. Provincia o departamente destinatario del envío (variable nacida de sección 1)
tres_transporte = 0 #STR. Tipo de transporte seleccionado (variable nacida de sección 3)

# NOTA: ya que tenemos el diccionario de referencia, acordemos que los nombres de todas las variables tengan un máximo de 2 palabras y lo más abreviadas posible (EJ: color, altura_base, cant_max) para mayor agilidad, pero siempre manteniéndose entendibles
# NOTA2: para variables "nacidas en una sección en particular" (que obtuvieron su primer input en X sección), colocar el número de sección al principio del nombre ("uno_xyz", "dos_xyz", "tres_xyz", "cuatro_xyz") ayudará con el debugging más tarde si la variable se reutiliza en otra parte, ya que se sabe desde dónde empezar a seguir su transformación



# Recuerden mantener buena ortografía y espaciado en los textos que se muestran al usuario
print("\n---------------------------------------------------------------------")
print("    ¡Bienvenido al cotizador de exportación de SmartRoast S.A.!\nIntroduzca la información de su pedido y se le devolverá la cantidad\nexacta que pagaría por el total de la operación, incluyendo costos\nde aduana e impuestos.")
print("---------------------------------------------------------------------\n")

# SECCIÓN 1: Destino
# pregunta al cliente los distintos datos sobre la dirección de destino en el siguiente orden: país (ofrece lista de opciones: Argentina, Bolivia, Uruguay), provincia/departamento (si el input anterior fue Argentina entonces pregunta por provincia, si fue Bolivia o Uruguay pregunta por departamente). Añadir distintas cantidades al acumulador principal "precio_fin" según las opciones seleccionadas (usar números cualquiera por ahora)
print("****************** DESTINO ******************")
print("limpiado")
print("*********************************************\n")


# SECCIÓN 2: Peso
# pregunta al cliente el peso del pedido en kilogramos. Añadir distintas cantidades al acumulador principal "precio_fin" según las opciones seleccionadas (usar números cualquiera por ahora)
print("****************** PESO ******************")
print("limpiado")
print("*********************************************\n")

# SECCIÓN 3: Transporte
# pregunta al cliente qué tipo de transporte desea según el país de Destino que eligió antes: si es en Argentina solo aparece opción terrestre, si es en cualquier otro puede elegir entre terrestre o aéreo. Añadir distintas cantidades al acumulador principal "precio_fin" según las opciones seleccionadas (usar números cualquiera por ahora)
print("****************** TRANSPORTE ******************")
print("limpiado")
print("*********************************************\n")


# SECCIÓN 4: Recargos
# utiliza la información de Destino para saber qué recargos aduaneros aplicar (para esto, se pueden usar condicionales para aplicar distintos recargos según el país de destino). Añadir distintas cantidades al acumulador principal "precio_fin" según las opciones seleccionadas (usar números cualquiera por ahora)
print("****************** RECARGOS ******************")
print("limpiado")
print("*********************************************\n")



# SECCIÓN 5: Ticket y QC
# muestra el ticket con precio final y un desglose de los costos de cada sección. Realiza pruebas hasta romper el sistema y luego añade parches para evitar dichos errores

print("La 1ra práctica individual ha concluido.\nTodos saben realizar commits a GitHub por su cuenta")
print("---------------------------------------------------------------------")