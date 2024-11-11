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

resultado = "pessoa1" in contatos
print(resultado)

resultado = "telefone" in contatos["pessoa1"]
print(resultado)

resultado = "idade" in contatos["pessoa1"]
print(resultado)
