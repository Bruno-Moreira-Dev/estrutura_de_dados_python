conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4, 1, 5, 6, 7}

conjunto_a_nao_pertence_b = conjunto_a.issuperset(conjunto_b)

conjunto_b_nao_pertence_a = conjunto_b.issuperset(conjunto_a)

print(conjunto_a_nao_pertence_b)
print(conjunto_b_nao_pertence_a)
