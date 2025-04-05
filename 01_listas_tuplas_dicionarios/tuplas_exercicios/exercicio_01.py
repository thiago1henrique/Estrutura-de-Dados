from random import randint

print("Exercicio 1")
x = 0
tupla = (randint(1,100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))

print(f"Os valores da tupla é {tupla}")

maiorValor = max(tupla);
menorValor = min(tupla);
print(f"O maior valor é {maiorValor}")
print(f"O menor valor é {menorValor}")
print("\n")