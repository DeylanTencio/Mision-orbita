# ============================================================
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Deylan Tencio
# Fecha: 27/10/2026        Versión: 1.0
# Descripción: Verifica el combustible de la nave y advierte cuando el
#              margen adicional después de cubrir la misión es bajo.
# ============================================================

# --------- constantes ---------
RESERVA_COMBUSTIBLE = 10
MARGEN_MINIMO_ADICIONAL = 10

# --------- entrada de datos ---------
combustible_disponible = int(input( "Ingrese la cantidad de combustible disponible: "))
combustible_requerido = int(input( "Ingrese la cantidad de combustible requerido para llegar al destino: "))
combustible_regreso = int(input("Ingrese la cantidad de combustible requerido para regresar al punto de origen: "))

# --------- procesamiento de datos ---------
combustible_total = combustible_requerido + combustible_regreso + RESERVA_COMBUSTIBLE
combustible_adicional = combustible_disponible - combustible_total

# --------- salida de datos ---------
print()
print("combustible disponible:", combustible_disponible, "unidades")
print("combustible requerido para llegar:", combustible_requerido, "unidades")
print("combustible requerido para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_COMBUSTIBLE, "unidades")
print("combustible total requerido:", combustible_total, "unidades")
print( "combustible adicional disponible:", combustible_adicional, "unidades")

#---------- decisión sobre el combustible adicional ----------
# la advertencia se muestra si el margen minimo adicional no se cumple.
if combustible_adicional < MARGEN_MINIMO_ADICIONAL:
    print("Advertencia: El margen adicional de combustible es bajo")


