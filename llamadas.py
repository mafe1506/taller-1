def calcular_costo_llamada(duracion_llamada, costo_por_minuto, descuento):
    costo_sin_descuento = duracion_llamada * costo_por_minuto
    costo_con_descuento = costo_sin_descuento * (1 - descuento)
    return costo_con_descuento

# Costos por minuto para diferentes países (en dólares)
costo_por_minuto_usa = 900
costo_por_minuto_canada = 800
costo_por_minuto_europa = 950
costo_por_minuto_resto_mundo = 1250

# Duración de la llamada en minutos
duracion_llamada = 15

# Descuento del 20%
descuento = 0.20

# Calcular costo total con descuento para diferentes países
costo_total_usa = calcular_costo_llamada(duracion_llamada, costo_por_minuto_usa, descuento)
costo_total_canada = calcular_costo_llamada(duracion_llamada, costo_por_minuto_canada, descuento)
costo_total_europa = calcular_costo_llamada(duracion_llamada, costo_por_minuto_europa, descuento)
costo_total_resto_mundo = calcular_costo_llamada(duracion_llamada, costo_por_minuto_resto_mundo, descuento)

# Mostrar resultados
print(f"Costo total de la llamada a Estados Unidos: ${costo_total_usa:.2f}")
print(f"Costo total de la llamada a Canadá: ${costo_total_canada:.2f}")
print(f"Costo total de la llamada a Europa: ${costo_total_europa:.2f}")
print(f"Costo total de la llamada al Resto del Mundo: ${costo_total_resto_mundo:.2f}")







