def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def retorna_vazio():
    print("Hello World!")
    return None

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))
print(retorna_vazio())
