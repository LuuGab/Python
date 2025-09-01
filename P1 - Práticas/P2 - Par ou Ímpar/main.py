# list(range(início, intervalo, passo))
start = int(input("Digite o valor de início: "))
intervalo = int(input("Digite o valor do intervalo: "))
step = int(input("Digite o valor do passo: "))

lista1 = list(range(start, intervalo, step))
lista2 = [x for x in lista1 if x % 2 == 0]
lista3 = [x for x in lista1 if x % 2 == 1]

if len(lista2) > 0:
    print("\n— [Números Pares]")
    for indice2, elemento2 in enumerate(lista2):
        print(f"• Índice: {indice2} | Elemento: {elemento2}")
else:
    print("\nNão houveram números pares.")

if len(lista3) > 0:
    print("\n— [Números Ímpares]")
    for indice, elemento in enumerate(lista3):
        print(f"• Índice: {indice} | Elemento: {elemento}")
else:
    print("\nNão houveram números ímpares.")