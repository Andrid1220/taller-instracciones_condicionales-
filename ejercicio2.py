# Definir la cantidad mínima de ingresos para calificar para el préstamo
MIN_INGRESOS = 945200

# Definir el estado de la deuda actual del prestatario
tiene_deuda = False

# Obtener los ingresos del prestatario del usuario
ingresos = float(input("Ingrese sus ingresos mensuales: "))

# Obtener el estado de la deuda del prestatario del usuario
respuesta = input("¿Tiene alguna otra deuda pendiente? (si / no): ")
if respuesta.lower() == "si":
    tiene_deuda = True

# Comprobar si el prestatario califica para el préstamo
if ingresos >= MIN_INGRESOS and not tiene_deuda:
    print("Felicitaciones, usted califica para el préstamo.")
else:
    print("Lo siento, usted no califica para el préstamo.")