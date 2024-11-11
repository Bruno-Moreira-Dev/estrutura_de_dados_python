contatos = {
    "pessoa1": {
        "nome": "Bruno",
        "telefone": "1234-5678"
    },
    "pessoa2": {
        "nome": "Joaquim",
        "telefone": "4321-8765"
    }
}

contatos.update({"pessoa1": { "nome": "Br", "telefone": "9999-9999" }})

print(contatos)

contatos.update({"pessoa3": { "nome": "Guilherme", "telefone": "8765-4321" }})

print(contatos)
