componentes = ["alas", "fuselaje", "motores"]
print(id(componentes))  # Guardamos el ID original

# Modificamos la lista
componentes.append("tren de aterrizaje")
print(componentes)  # ["alas", "fuselaje", "motores", "tren de aterrizaje"]
print(id(componentes))  # Mismo ID, el objeto fue modificado in-place


# ❓¿Cómo afecta la mutabilidad a los objetos que se usan como argumentos de una función?

def agregar_combustible(tanques, litros):
    tanques.append(litros) #lo hallade a la lista 
    print(f"Combustible actualizado: {tanques}") 

combustible_actual = [1000, 1200, 800]  # Lista (objeto mutable)
agregar_combustible(combustible_actual, 500)
print(combustible_actual)  # [1000, 1200, 800, 500] - La lista original fue modificada