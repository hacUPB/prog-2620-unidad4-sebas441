# **¿Qué es un iterable?**
# Un iterable es cualquier objeto Python sobre el cual podemos recorrer sus elementos uno por uno. Técnicamente,
#  un iterable es cualquier objeto que implementa el método "__iter__()"" o "__getitem__()""

# Iterando sobre una lista de sensores de aeronave
#  sensores = ["temperatura", "presión", "velocidad", "altitud", "combustible"]

#  for sensor in sensores:
#      print(f"Comprobando sensor de {sensor}...")



# ¿Que pasaria si esto se hiciera con un while?
# Simulando lecturas de altitud cada 10 segundos

altitudes = [0, 100, 500, 1000, 1500, 2000, 2200, 2500]
tiempo = 0
i = 0

while i < len(altitudes):    #len devuelve los elementos que tienes en la lista 
    print(f"Tiempo: {tiempo}s - Altitud: {altitudes[i]} metros")
    tiempo += 10
    i += 1
