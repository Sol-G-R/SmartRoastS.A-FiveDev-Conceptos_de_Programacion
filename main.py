# Diccionario de variables (TODAS las variables que usen deben registrarse acá, con sus tipos y propósitos)

precio_fin = 0 #FLOAT. Cantidad de plata que se le mostrará al cliente en el ticket (variable acumuladora que se pasa de sección a sección)
dist_prov = 0 #STR. Provincia destinataria del envío

# NOTA: ya que tenemos el diccionario de referencia, acordemos que los nombres de todas las variables tengan un máximo de 2 palabras y lo más abreviadas posible (EJ: color, altura_base, cant_max) para mayor agilidad, pero siempre manteniéndose entendibles




# Recuerden mantener buena ortografía y espaciado en los textos que se muestran al usuario
print("¡Bienvenido al cotizador de exportación de SmartRoast S.A.!\nIntroduzca la información de su pedido y se le devolverá la cantidad exacta que pagaría por el total de la operación, incluyendo costos de aduana e impuestos.")


# SECCIÓN 1: Destino
# pregunta al cliente los distintos datos sobre la dirección de destino en el siguiente orden: país (ofrece lista de opciones: Argentina, Chile, Bolivia, Uruguay), provincia, ciudad. Añadir distintas cantidades al acumulador principal "precio_fin" según las opciones seleccionadas (usar números cualquiera por ahora)



# SECCIÓN 2: Peso
# pregunta al cliente el peso del pedido en kilogramos. Añadir distintas cantidades al acumulador principal "precio_fin" según las opciones seleccionadas (usar números cualquiera por ahora)



# SECCIÓN 3: Transporte
# pregunta al cliente qué tipo de transporte desea según el país de Destino que eligió antes: si es en Argentina solo aparece opción terrestre, si es en cualquier otro puede elegir entre terrestre o aéreo. Añadir distintas cantidades al acumulador principal "precio_fin" según las opciones seleccionadas (usar números cualquiera por ahora)



# SECCIÓN 4: Recargos
# utiliza la información de Destino para saber qué recargos aduaneros aplicar. 



# SECCIÓN 5: Ticket y QC
# muestra el ticket con precio final y un desglose de los costos de cada sección. Realiza pruebas hasta romper el sistema y aplica Try-Excepts para evitar dichos errores