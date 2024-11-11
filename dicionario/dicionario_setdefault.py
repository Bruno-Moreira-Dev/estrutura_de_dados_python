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

contatos.setdefault("nome", "Luana")
contatos.setdefault("idade", 29)

print(contatos)
