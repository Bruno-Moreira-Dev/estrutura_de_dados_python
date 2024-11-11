pessoa = {"nome": "Bruno", "idade": 29}

print(pessoa)

pessoa = dict(nome="Bruno", idade=29)

print(pessoa)

pessoa["telefone"] = "1234-5678"

print(pessoa)

print(pessoa["nome"])
print(pessoa.get("telefone"))
