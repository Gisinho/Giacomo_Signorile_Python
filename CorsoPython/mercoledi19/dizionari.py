studente = {
    "nome":"Alice",
    "età":20,
    "sesso":"Femmina"
}

print(studente["nome"])
print(studente["età"])

studente["nome"] = "Filippo"
studente["città"] = "Roma"


print(studente.keys())
print(studente.values())
print(studente.items())

print(studente.get("nome"))

print(studente)