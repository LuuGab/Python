#Estruturas de Dados



#- Listas (list) -> ORDENADO; MUTÁVEL; PERMITE ELEMENTOS DUPLICADOS
print(f"-"*50)
lista = ["Item 01", 2, 4.2, True]
print(f"Tipo da Estrutura: {type(lista)}")

for indice, elemento in enumerate(lista):
    print(f"• Índice: {lista.index(elemento)} | Type: {type(lista[indice])}| Elemento: {elemento}")



#- Tuplas (tuple) -> ORDENADO; IMUTÁVEL; PERMITE ELEMENTOS DUPLICADOS
print(f"-"*50)
tupla = ("Item 01", 2, 4.2, True)
print(f"Tipo da Estrutura: {type(tupla)}")

for x,y in enumerate(tupla):
    print(f"• Posição: {tupla.index(y)} | Type: {type(tupla[x])}| Item: {y}")



#- Dicionário (dict) -> ORDENADO; MUTÁVEL; NÃO PERMITE ELEMENTOS DUPLICADOS

#Observação: A chave de um dicionário pode, e frequentemente é, um tipo de dado primitivo, pois ela deve ser um tipo de dado imutável. Como strings ou inteiros.
print(f"-"*50)
dicionario = {
    "chave 01": "Valor 01",
    "chave 02": 2,
    "chave 03": 4.2,
    "chave 04": True,
    "chave 05": ["elemento 01", 2, 3.14],
    "chave 06": ("Item 01", 2, 3.14)
    }
print(f"Tipo da Estrutura: {type(dicionario)}")

for x,y in enumerate(dicionario):
    print(f"• Posição: {x} | Type: {type(dicionario[y])}| Chave: {y} | Item: {dicionario[y]}")



#- Conjuntos (set) -> DESORDENADO; NÃO INDEXADO (Não possui identificador das posições do elementos internos); NÃO PERMITE ELEMENTOS DUPLICADOS
print(f"-"*50)
conjunto = {"Item 01", 2, 3.14, True, ("Item 01", 2, 3.14),}
print(f"Tipo da Estrutura: {type(conjunto)}")
print(f"{conjunto}")
print(f"-"*50)