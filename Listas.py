# Lista vacía
# componentes = []

# Lista con elementos
# componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"]

# Lista con diferentes tipos de datos
# datos_vuelo = [202, "Boeing 737", True, 10500.5]

# Listas anidadas
# matriz_rotacion = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"]

# print(componentes[-1]) # el -1 es contar de atras para delante es decir en este caso sería el último en la lista "tren de aterrizaje"

# componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"]

# print(componentes[2:4])



  
# lista = []

# llenar la lista con 10 datos iguales 
# for i in range(10):
#    lista.append("hallo")

# print(lista)


# Ahora llenar la lista con 10 datos diferentes 

# lista = []

# for i in range(3):
#     lista.append(int(input(f"Ingrese #{i+1} a la lista")))
# print(lista)

# Datos de vuelo para un avión comercial
tiempo = [0, 10, 20, 30, 40, 50, 60]  # segundos
altitud = [0, 100, 500, 1000, 1500, 2000, 2200]  # metros
velocidad = [0, 50, 100, 150, 200, 250, 300]  # km/h
estado = ["despegue", "ascenso inicial", "ascenso", "ascenso", "ascenso", "nivelación", "crucero"]

# Imprimir informe de despegue
print("INFORME DE DESPEGUE:")
for t, a, v, est in zip(tiempo, altitud, velocidad, estado):
    print(f"T+{t}s: Altitud={a}m, Velocidad={v}km/h, Fase={est}")