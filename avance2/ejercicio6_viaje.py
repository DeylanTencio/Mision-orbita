# ============================================================
# Archivo: ejercicio6_viaje.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Deylan Tencio
# Fecha: 09/11/2026        Versión: 1.0
# Descripción: Simula día a día el viaje de la nave hacia el destino.
# ============================================================

# ----------- constantes -----------
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_ENERGIA_DIA = 5
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1 

# ----------- Entradas -----------
dias_viaje = int(input("Ingrese la cantidad de dias del viaje:"))
tripulantes = int(input("Ingrese la cantidad de tripulantes:"))
combustible = int(input("Ingrese el combustible disponible:"))
oxigeno = int(input( "Ingrese el oxigeno disponible:"))
energia = int(input("Ingrese la energia disponible:"))
provisiones = int(input("Ingrese las provisiones disponibles:"))

# ----------- Inicializacion -----------
# El consumo diario depende de la cantidad de tripulantes
consumo_oxigeno_dia = tripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA 
consumo_provisiones_dia = tripulantes * CONSUMO_PROVISIONES_TRIPULANTE_DIA
dias_transcurridos = 0 #contador dias completados
puede_continuar = True #bandera: Pasa a falsa si faltan recursos

print()

# ----------- Ciclo: Cada vuelta es un dia del viaje -----------
while dias_transcurridos < dias_viaje and puede_continuar:
    # Se revisa antes de gastar, para no quedar en negativo
    if (combustible >= CONSUMO_COMBUSTIBLE_DIA 
        and oxigeno >= consumo_oxigeno_dia
        and energia >= CONSUMO_ENERGIA_DIA
        and provisiones >= consumo_provisiones_dia):
        combustible = combustible - CONSUMO_COMBUSTIBLE_DIA
        oxigeno = oxigeno - consumo_oxigeno_dia
        energia = energia - CONSUMO_ENERGIA_DIA
        provisiones = provisiones - consumo_provisiones_dia
        dias_transcurridos = dias_transcurridos + 1 
        print (f"Dia {dias_transcurridos}: combustible: {combustible}, oxigeno: {oxigeno}, energia: {energia}, provisiones {provisiones}")

    else: 
        puede_continuar = False

# ----------- Salida resultados -----------
if puede_continuar:
    print(f"La nave llego al destino en {dias_transcurridos} dias")
    print(f"Combustible restante: {combustible} unidades")
    print(f"Oxigeno restante: {oxigeno} unidades")
    print(f"Energia restante: {energia} unidades")
    print(f"provisiones restantes: {provisiones} unidades")

else:
    dia_fallido = dias_transcurridos + 1
    print(f"viaje interrumpiddo en el dia, {dia_fallido}")
    # Se revisa cada recurso por separado: puede faltar mas de uno a la vez
    if combustible < CONSUMO_COMBUSTIBLE_DIA:
        print("Recurso insuficiente: combustible")
    if oxigeno < consumo_oxigeno_dia:
        print("Recurso insuficiente: oxigeno")
    if energia < CONSUMO_ENERGIA_DIA:
        print("Recurso insuficiente: energia")
    if provisiones < consumo_provisiones_dia:
        print("Recurso insuficiente: provisiones")
    print(f"dias completados: {dias_transcurridos}")





    
