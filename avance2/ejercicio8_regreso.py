# ============================================================
# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Deylan Tencio
# Fecha: 09/11/2026        Versión: 1.0
# Descripción: Evalúa si la nave puede regresar. Si puede, simula el
#              regreso día a día; si no, calcula los días de supervivencia.
# ============================================================

# ------------ Constantes -------------
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1

# ----------- Entrada de datos ------------
tripulantes = int(input("Ingrese la cantidad de tripulantes:"))
dias_viaje = int(input("Ingrese los dias del viaje de ida:"))
combustible = int(input("Ingrese el combustible disponible:"))
oxigeno = int(input("Ingrese el oxigeno disponible:"))
energia = int(input("Ingrese la energia disponible:"))
provisiones = int(input("Ingrese las provisiones disponibles:"))

# ----------- Procesamiento inicial ------------
# El regreso y la ida duran lo mismo (no se exige reserva en esta etapa)
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
consumo_oxigeno_dia = tripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA
consumo_provisiones_dia = tripulantes * CONSUMO_PROVISIONES_TRIPULANTE_DIA 

print()

# ----------- Decision: Regreso de la nave ------------
if combustible >= combustible_regreso: 
    # ===== CASO A: la nave puede regresar =====
    dias_transcurridos = 0
    puede_continuar = True

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
            print (f"Dia {dias_transcurridos}: combustible: {combustible}, oxigeno: {oxigeno}, energia: {energia}, provisiones: {provisiones}")

        else: 
            puede_continuar = False
    print() 
    if puede_continuar:
        print("La tripulacion regreso exitosamente a la Tierra")
        print(f"Combustible restante: {combustible} unidades")
        print(f"oxigeno restante: {oxigeno} unidades")
        print(f"Energia restante: {energia} unidades")
        print(f"Provisiones restantes: {provisiones} unidades")
    else:
        dia_fallido = dias_transcurridos + 1
        print(f"El regreso se interrumpio en el dia {dia_fallido}")
        # El combustible no se revisa
        if oxigeno < consumo_oxigeno_dia:
            print("Recurso insuficiente: oxigeno")
        if energia < CONSUMO_ENERGIA_DIA:
            print("Recurso insuficiente: energia")
        if provisiones < consumo_provisiones_dia:
            print("Recurso insuficiente: provisiones")
        print("La tripulacion no completo el regreso.")
else:
    print("La tripulacion quedo varada en el destino.")
# ===== CASO B: la nave queda varada =====

#Division entera (//): solo cuentan dias completos
    dias_oxigeno = oxigeno // consumo_oxigeno_dia
    dias_energia = energia // CONSUMO_ENERGIA_DIA 
    dias_provisiones = provisiones // consumo_provisiones_dia

    # Busqueda del minimo sin min(): se asume que el primero es el menor
    # y se compara contra cada uno de los otros
    supervivencia = dias_oxigeno
    if dias_energia < supervivencia:
        supervivencia = dias_energia 
    if dias_provisiones < supervivencia:
        supervivencia = dias_provisiones

    #Recursos Limitantes
    recursos_limitantes = ""
    if dias_oxigeno == supervivencia:
        recursos_limitantes = "oxigeno"
    if dias_energia == supervivencia: 
        if recursos_limitantes == "":
            recursos_limitantes = "energia"
        else:
            recursos_limitantes = recursos_limitantes + ", energia"
    if dias_provisiones == supervivencia:
        if recursos_limitantes == "":
            recursos_limitantes = "provisiones"
        else:
            recursos_limitantes = recursos_limitantes + ", provisiones"


    print(f"Dias por oxigeno {dias_oxigeno}")
    print(f"Dias por energia {dias_energia}")
    print(f"Dias por provisiones {dias_provisiones}")
    print(f"Supervivencia estimada: {supervivencia} dias")
    print(f"Recurso(s) limitante(s): {recursos_limitantes}")
   


