print("Exercicio 4")

a, b, c, d = input("Insira os 4 valores: ").split()

valores = (int(a), int(b), int(c), int(d))

contadorNove = 0
exibeCasaTres = None
valoresPares = []

for indice, valor in enumerate(valores):
    if valor == 9:
        contadorNove += 1

    if valor == 3 and exibeCasaTres is None:
        exibeCasaTres = indice

    if valor % 2 == 0:
        valoresPares.append(valor)

print(f"Foi insirido {contadorNove} vezes o valor 9")
print(f"O primeiro valor 3 foi inserido na chave {exibeCasaTres}")
print(f"Os números pares são {valoresPares}")