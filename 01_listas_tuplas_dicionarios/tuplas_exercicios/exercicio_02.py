print("Exercicio 2")

times_brasileirao = (
    'Palmeiras',
    'Grêmio',
    'Atlético-MG',
    'Flamengo',
    'Botafogo',
    'Bragantino',
    'Fluminense',
    'Athletico-PR',
    'Internacional',
    'Fortaleza',
    'São Paulo',
    'Cuiabá',
    'Corinthians',
    'Cruzeiro',
    'Vasco',
    'Bahia',
    'Santos',
    'Goiás',
    'Coritiba',
    'América-MG'
)

print("Os 5 primeiros colocados do Brasilerão 2023")
for x in times_brasileirao[0:5]:
    print(x)

print("\n")
print("Os 4 ultimos colocados do Brasilerão 2023")
for y in times_brasileirao[-4:]:
    print(y)

print("Lista em ordem alfabetica")
times_alfabetico = sorted(times_brasileirao)
print(times_alfabetico)
print("\n")

print("Exibe colocação Santos")
x = 0
for time in times_brasileirao:
    x += 1
    if time == "Santos":
        print(f"O santos está  na posição: {x}")