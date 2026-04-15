# list.insert( i, x)
# list.remove(x)
# list.pop([i])

numero = [0,20,30,40]
numero.insert(4,50)
print("Despues del insert", numero)

numero.remove(30)
print("Despues del remove", numero)

eliminado = numero.pop (3)
print("elemento eliminado con pop", eliminado)
print("Despues del pop", numero)
