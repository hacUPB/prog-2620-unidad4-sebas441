# Representando una flota de aeronaves con tuplas
# (modelo, envergadura (m), longitud (m), mtow (kg), velocidad_max (km/h))
fleet_data = [
    ("Airbus A320", 35.80, 37.57, 78000, 871),
    ("Boeing 737-800", 35.79, 39.47, 79010, 853),
    ("Embraer E190", 28.72, 36.24, 51800, 871),
    ("Bombardier CRJ-900", 24.85, 36.40, 38330, 870)
]

# fleet_data[0] = 5

# print(fleet_data)

# print(fleet_data[2][0])

tupla_lista = (1, 4, [4,5,8])

tupla_lista[2][0] = 222

print(tupla_lista[2])

