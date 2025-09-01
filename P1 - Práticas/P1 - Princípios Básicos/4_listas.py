# List | List é uma coleção ordenada de elementos e indíces. Isto é, o item em questão, e o valor representativo de sua posição dentro da coleção, tal qual começa em 0.
lista_de_compras = []
continuar = True

#While | Enquanto uma condição for verdadeira o bloco do código será repetido.
while continuar!=False:
    resposta = input(("\nDeseja adicionar algum produto à lista? (S/N): "))
    if resposta.upper() == "S":
        item = input(("Digite o nome de uma mercadoria: "))
        lista_de_compras.append(item)
    elif resposta.upper() == "N":
        continuar = False
    else:
        print("Resposta Inválida.")

#For Each | Estrutura utilizada para iterar uma sequência de itens sejam eles listas, tuplas ou dicionários.
print(f"Quantidade de Itens: {len(lista_de_compras)} | Itens da Lista:")
for x in lista_de_compras:
    numero_item = int(lista_de_compras.index(x)) + 1
    print(f"• Índice: {lista_de_compras.index(x)} | N°: {numero_item} | Item: {x}")