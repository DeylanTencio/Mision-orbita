# ============================================================
# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Deylan Tencio
# Fecha: 27/10/2026        Versión: 1.0
# Descripción: Verifica si la nave tiene oxígeno y provisiones suficientes
#              para mantener a la tripulación durante el viaje.
# ============================================================

# --------- entrada de datos ---------
oxigeno_disponible = int(input("Oxigeno disponible:"))
oxigeno_requerido = int(input("oxigeno requerido:"))
provisiones_disponibles = int(input("Provisiones disponibles:"))
provisiones_requeridas = int(input("Provisiones requeridos:"))

print()

# --------- decision doble ---------
# se usa "and" porque la tripulacion necesita AMBOS recursos a la vez.
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave tiene recursos suficientes para la tripulacion")
else:
    print("La nave no cuenta con los recursos necesarios para la tripulacion")
