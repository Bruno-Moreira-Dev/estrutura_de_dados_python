numeros = [1, 30, 21, 5, 9]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

novo_pares = [numero for numero in numeros if numero % 2 == 0]
print(novo_pares)
