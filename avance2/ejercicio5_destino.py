# ============================================================
# Archivo: ejercicio5_destino.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Deylan Tencio
# Fecha: 05/11/2026        Versión: 1.0
# Descripción: Permite seleccionar el destino de la misión, determina
#              la duración del viaje y decide si se autoriza el lanzamiento.
# ============================================================

# ----------- constantes -----------
from unittest import case


CONSUMO_COMBUSTIBLE_DIA = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
EMERGENCIA_OXIGENO = 5
CONSUMO_ENERGIA_DIA = 5
ENERGIA_EXPLORACION = 10
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1
PROVISIONES_ADICIONALES = 3
DIAS_LUNA = 3
DIAS_MARTE = 5
DIAS_EUROPA = 7

#----------- Entrada de datos -----------
nombre_mision = input("Ingrese el nombre de la mision:")
tripulantes = int(input("Ingrese la cantidad de tripulantes:"))
print ("Destinos disponibles: ")
print ("1.Luna")
print("2.Marte")
print("3.Europa")
opcion_destino = int(input("Seleccione el destino:"))
combustible_disponible = int(input("combustible disponible: "))
oxigeno_disponible = int(input("Oxigeno disponible:"))
energia_disponible = int(input("Energia disponible:"))
provisiones_disponibles = int(input("Provisiones disponibles:"))

# ----------- Inicializacion -----------
destino = ""
dias_mision = 0
opcion_valida = True

# ---------- seleccion del destino ----------
match opcion_destino: 
    case 1:
        destino = "Luna"
        dias_mision = DIAS_LUNA
    case 2:
        destino = "Marte"
        dias_mision = DIAS_MARTE
    case 3: 
        destino = "Europa"
        dias_mision = DIAS_EUROPA 
    case _:
        opcion_valida = False

# ----------- calculo y autorizacion -----------
if opcion_valida:
    # El regreso dura lo mismo que la ida
    combustible_ida = dias_mision * CONSUMO_COMBUSTIBLE_DIA
    combustible_regreso = dias_mision * CONSUMO_COMBUSTIBLE_DIA
    combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
    oxigeno_requerido = dias_mision * tripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA + EMERGENCIA_OXIGENO
    energia_requerida = dias_mision * CONSUMO_ENERGIA_DIA + ENERGIA_EXPLORACION
    provisiones_requeridas = dias_mision * tripulantes * CONSUMO_PROVISIONES_TRIPULANTE_DIA + PROVISIONES_ADICIONALES 

    # Resumen de la mision
    print()
    print("Mision:", nombre_mision)
    print("Destino:", destino) 
    print ("Cantidad de tripulantes:", tripulantes)
    print("Duracion dle viae de ida:", dias_mision, "dias")
    print("combustible requerido para llegar:", combustible_ida, "unidades")
    print( "combustible requerido para el regreso:", combustible_regreso, "unidades")
    print("Combustible de reserva:", RESERVA_COMBUSTIBLE, "unidades")
    print( "Oxigeno requerido:", oxigeno_requerido, "unidades")
    print("Energia requerida:", energia_requerida, "unidades")
    print( "Porivisiones requeridas:", provisiones_requeridas, "unidades")

    # Autorizacion del ejercicio 4 (decision anidada)
    if (combustible_disponible >= combustible_total
        and oxigeno_disponible >= oxigeno_requerido
        and energia_disponible >= energia_requerida
        and provisiones_disponibles >= provisiones_requeridas):
        print("lanzamiento autorizado.")
    else:
        print("Lanzamiento no autorizado. La mision debe ser revisada.")
else:
    print("Opcion de destino no valida. La mision no puede planficarse.")