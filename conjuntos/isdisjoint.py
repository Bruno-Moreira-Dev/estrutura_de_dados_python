conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a_nenhum_element_pertence_b = conjunto_a.isdisjoint(conjunto_b)
conjunto_a_nenhum_element_pertence_c = conjunto_a.isdisjoint(conjunto_c)

print(conjunto_a_nenhum_element_pertence_b)
print(conjunto_a_nenhum_element_pertence_c)
