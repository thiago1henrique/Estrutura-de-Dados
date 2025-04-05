tabela = {
    "Alface": 0.45,
    "Batata": 1.20,
    "Tomate": 2.30,
    "Feijão": 1.50,

}

d = {}
for letra in "estrutura":
    d[letra] = d.get(letra, 0) + 1
print(d)