# ============================================================
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Deylan Tencio
# Fecha: 27/10/2026        Versión: 1.0
# Descripción: Verificación general de recursos antes de autorizar
#              el lanzamiento de la misión.
# ============================================================

# --------- constantes ---------
RESERVA_COMBUSTIBLE = 10

# --------- entrada de datos ---------
combustible_disponible = int(input("combustible disponible: "))
combustible_ida = int(input("combustible requerido para llegar al destino:"))
combustible_regreso = int(input("Combustible requerido para regresar:"))
oxigeno_disponible = int(input("Oxigeno disponible:"))
oxigeno_requerido = int(input("Oxigeno requerido:"))
energia_disponible = int(input("Energia disponible:"))
energia_requerida = int(input("Energia requerida:"))
provisiones_disponibles = int(input("Provisiones disponibles:"))
provisiones_requeridas = int(input("provisiones requeridas:"))

# --------- procesamiento de datos ---------
# se exige desde el inicio combustible de ida, de regreso y la reserva
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE 

print()
print("Combustible total requerido:", combustible_total, "unidades")

# ------------ Decision doble ------------
# Los cuatro recursos deben alcanzar; si falla uno solo no se autoriza.
if (combustible_disponible >= combustible_total
    and oxigeno_disponible >= oxigeno_requerido
    and energia_disponible >= energia_requerida
    and provisiones_disponibles >= provisiones_requeridas):
    print ("lanzamiento autorizado.")

else:
    print ("lanzamiento no autorizado. La mision debe ser revisada.")

