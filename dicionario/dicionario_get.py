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

telefone_pessoa1 = contatos.get("pessoa1", {}).get("telefone")

print(telefone_pessoa1)
