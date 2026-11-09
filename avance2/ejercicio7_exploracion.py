# ============================================================
# Archivo: ejercicio7_exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Deylan Tencio
# Fecha: 09/11/2026        Versión: 1.0
# Descripción: Menú repetitivo de actividades de exploración científica
#              con contadores y acumulador de puntos.
# ============================================================

# ----------- constantes -----------
ENERGIA_ANALIZAR = 8
PROVISIONES_ANALIZAR = 0
PUNTOS_ANALIZAR = 10

ENERGIA_RECOLECTAR = 12
PROVISIONES_RECOLECTAR = 2
PUNTOS_RECOLECTAR = 20

ENERGIA_OBSERVAR = 5
PROVISIONES_OBSERVAR = 0
PUNTOS_OBSERVAR = 8

# ----------- Entrada de datos -----------
energia = int(input( "Ingrese la energia disponible:"))
provisiones = int(input("Ingrese las provisiones disponibles:"))

# ---------- Inicializacion -----------
puntos_cientificos  = 0 #acumulador puntos
actividades_realizadas = 0 # contador actividades
muestras_recolectadas = 0 # contador de muestras
explorando = True #bandera que controla menu

# ---------- ciclo: el menu se repite mientras se explora -----------
while explorando :
    print()
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print ("3. Realizar observacion")
    print("4. Finalizar exploracion")
    opcion = int(input("Seleccione una actividad:"))

    match opcion:
        case 1:
        # se revisa el alcance de los recursos primero
            if energia >= ENERGIA_ANALIZAR and provisiones >= PROVISIONES_ANALIZAR:
                energia = energia - ENERGIA_ANALIZAR
                provisiones = provisiones - PROVISIONES_ANALIZAR 
                actividades_realizadas = actividades_realizadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_ANALIZAR
                print("Actividad realizada: Analizar terreno. Puntos obtenidos:", PUNTOS_ANALIZAR)
            else:
                print("Recursos insuficientes para realizar la actividad. La exploracion finaliza.")
                explorando = False

        case 2:
            if energia >= ENERGIA_RECOLECTAR and provisiones >= PROVISIONES_RECOLECTAR:
                energia = energia - ENERGIA_RECOLECTAR
                provisiones = provisiones - PROVISIONES_RECOLECTAR
                actividades_realizadas = actividades_realizadas + 1
                muestras_recolectadas = muestras_recolectadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_RECOLECTAR
                print("Actividad realizada: Recolectar muestra. Puntos obtenidos:", PUNTOS_RECOLECTAR)
            else:
                print("Recursos insuficientes para realizar la actividad. La exploracion finaliza.")
                explorando = False

        case 3:
            if energia >= ENERGIA_OBSERVAR and provisiones >= PROVISIONES_OBSERVAR:
                energia = energia - ENERGIA_OBSERVAR
                provisiones = provisiones - PROVISIONES_OBSERVAR
                actividades_realizadas = actividades_realizadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_OBSERVAR
                print("Actividad realizada: Realizar observacion. Puntos obtenidos:", PUNTOS_OBSERVAR)
            else:
                print("Recursos insuficientes para realizar la actividad. La exploracion finaliza.")
                explorando = False
        
        case 4: 
            explorando = False

        case _: 
            print("Opcion no valida")
                    
# ------------- salidas ---------------
print()   
print(f"Actividades realizadas: {actividades_realizadas}")             
print(f"Muestras recolectadas: {muestras_recolectadas}.")
print(f"Puntos cientificos: {puntos_cientificos}.")
print(f"Energia restante: {energia} unidades.")
print(f"Provisiones restantes: {provisiones} unidades.")                 


