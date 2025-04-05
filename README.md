## Tuplas
* escreva aqui
---
## Dicionários 
* São similares às listas, no entanto, com propriedades de acesso diferentes;
* Dicionários são compostos de chaves e valores, acessociando uma chave a um valor
* Criar um deicionário usamos `{}`, cada elemento é um par de chave, valor
### Exemplo de dicionário 

```python
tabela = {
    "Alface": 0.45,
    "Batata": 1.20,
    "Tomate": 2.30,
    "Feijão": 1.50
}

tabela["Alface"] # 0.45
tabela["Tomate"] # 2.30
tabela["Tomate"] = 10.0 # 10.0
print(tabela["Manga"]) #keyerror
```
### Métodos de Dicionários
```python
tabela = {
    "Alface": 0.45,
    "Batata": 1.20,
    "Tomate": 2.30,
    "Feijão": 1.50
}

print(tabela.keys()) #retona todas as chaves
print(tabela.values()) #retona todos valores da chaves
print(tabela.items()) #retona chave/valor

for k, v in tabela.items():
    print(f"{k}: {v}")
```
