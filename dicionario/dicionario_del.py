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

del contatos["pessoa1"]["telefone"]

print(contatos)

del contatos["pessoa2"]

print(contatos)
