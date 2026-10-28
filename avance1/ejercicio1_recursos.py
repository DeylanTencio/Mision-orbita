# ============================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Deylan Tencio
# Fecha: 27/10/2026        Versión: 1.0
# Descripción: Calcula los recursos necesarios para una misión.
# ============================================================

consumo_combustible_dia = 8
reserva_combustible = 2
consumo_oxigeno_tripulante_dia = 2
emergencia_oxigeno = 5
consumo_energia_dia = 5
energia_exploracion = 10
consumo_provisiones_tripulante_dia = 3
provisiones_adicionales = 3

# --------- Entra da de datos ---------
nombre_mision = input("Ingrese el nombre de la misión: ")
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_mision = int(input("Ingrese la cantidad de días para llegar al destino: "))

# --------- procesamiento de datos ---------
# la ida y el regreso tardan lo mismo por lo cual el consumo de combustible es el mismo.
combustible_ida = dias_mision * consumo_combustible_dia
combustible_regreso = dias_mision * consumo_combustible_dia
combustible_total = combustible_ida + combustible_regreso + reserva_combustible

# Oxigeno, energia y provisiones se calculan solo para el viaje de ida.
oxigeno_requerido = dias_mision * tripulantes * consumo_oxigeno_tripulante_dia + emergencia_oxigeno
energia_requerida = dias_mision * consumo_energia_dia + energia_exploracion
provisiones_requeridas = dias_mision * tripulantes * consumo_provisiones_tripulante_dia + provisiones_adicionales 

# --------- salida de datos ---------
print("Mision:", nombre_mision)
print("cantidad de tripulantes:", tripulantes)
print("Duracion estimada hasta el destino:", dias_mision, "dias")
print("combustible requerido para llegar:", combustible_ida, "litros")
print("combustible requerido para el regreso:", combustible_regreso, "litros")
print("combustible de reserva:", reserva_combustible, "litros")
print("combustible total requerido:", combustible_total, "litros")
print("oxigeno requerido:", oxigeno_requerido, "unidades")
print("Energia requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")