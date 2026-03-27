# Creación de un diccionario
vuelo = {}

vuelo = {
    "aerolínea" : "Avianca",
    "vuelo" : "AV123",
    "origen" : "BOG",
    "destino" : "MED"
}
print(vuelo)

# Acceso a los valores
vuelo["destino"] = "ciudad_llegada"
print(vuelo)

# Modificación de un valor existente
vuelo["destino"] = "CLO"
print(vuelo)

# Agregar un nuevo par clave-valor
vuelo["estado"] = "en el aire"
print(vuelo)

#Agregar un nuevo par clave-valor
piloto = vuelo.get("Piloto", "Piloto no asignado")
print(piloto)

# Eliminar un dato (clave y valor)
del vuelo["vuelo"]
print(vuelo)

