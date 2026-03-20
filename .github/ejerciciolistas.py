# Explicacion del import
# import random
# print(random.randint(2,10))


# Crear una lista con 100 números aleatorios entre 100 y 200

lista = []
for i in range(100):
     lista.append(random.randint(100,200))

print(lista)

# ahora que es max
# mayor = max(lista)
# print(f"El número más grande de la lista es {mayor}") 
# El max nos indica cual es el número mas grande de esa lista


# Implementar la función max usando un bucle

# inice = 0 
# may = lista[0]
# while indice < 99:
#     if may < lista[indice + 1]:
#         may = lista[indice + 1]
#     indice += 1 

# print(f"El mayor calculando a mano es: {may}")


# calcular el menor de todos 

inice = 0 
may = lista[0]
while indice < 99:
    if may < lista[indice + 1]:
        may = lista[indice + 1]
    indice += 1 

print(f"El mayor calculando a mano es: {may}")