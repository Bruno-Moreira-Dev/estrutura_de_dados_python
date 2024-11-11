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

copia = contatos.copy()
copia["pessoa1"] = {"nome": "Guilherme"}

print(copia)
