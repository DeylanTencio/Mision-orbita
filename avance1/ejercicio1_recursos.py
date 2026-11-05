# ============================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Deylan Tencio
# Fecha: 27/10/2026        Versión: 1.0
# Descripción: Calcula los recursos necesarios para una misión.
# ============================================================

CONSUMO_COMBUSTIBLE_DIA = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
EMERGENCIA_OXIGENO = 5
CONSUMO_ENERGIA_DIA = 5
ENERGIA_EXPLORACION = 10
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1
PROVISIONES_ADICIONALES = 3

# --------- Entrada de datos ---------
nombre_mision = input("Ingrese el nombre de la misión: ")
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_mision = int(input("Ingrese la cantidad de días para llegar al destino: "))

# --------- procesamiento de datos ---------
# la ida y el regreso tardan lo mismo por lo cual el consumo de combustible es el mismo.
combustible_ida = dias_mision * CONSUMO_COMBUSTIBLE_DIA
combustible_regreso = dias_mision * CONSUMO_COMBUSTIBLE_DIA
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Oxigeno, energia y provisiones se calculan solo para el viaje de ida.
oxigeno_requerido = dias_mision * tripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA + EMERGENCIA_OXIGENO
energia_requerida = dias_mision * CONSUMO_ENERGIA_DIA + ENERGIA_EXPLORACION
provisiones_requeridas = dias_mision * tripulantes * CONSUMO_PROVISIONES_TRIPULANTE_DIA + PROVISIONES_ADICIONALES 

# --------- salida de datos ---------
print("Mision:", nombre_mision)
print("cantidad de tripulantes:", tripulantes)
print("Duracion estimada hasta el destino:", dias_mision, "dias")
print("combustible requerido para llegar:", combustible_ida, "unidades")
print("combustible requerido para el regreso:", combustible_regreso, "unidades")
print("combustible de reserva:", RESERVA_COMBUSTIBLE, "unidades")
print("combustible total requerido:", combustible_total, "unidades")
print("oxigeno requerido:", oxigeno_requerido, "unidades")
print("Energia requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")
