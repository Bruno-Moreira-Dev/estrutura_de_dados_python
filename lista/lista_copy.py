lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(id(lista), id(lista.copy()))
print("Lista: ", lista)
print("Copia: ", lista.copy())
