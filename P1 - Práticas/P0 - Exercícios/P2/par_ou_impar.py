print("\n--- Par ou Ímpar ---")
valor_inicial = int(input("• Digite o valor de ínicio da contagem: "))
valor_final = int(input("• Digite o valor final da contagem: ")) + 1
step = int(input("• Digite o valor incrementável: "))

lista = list(range(valor_inicial, valor_final, step))
lista_par = list(x for x in lista if x % 2 == 0)
lista_impar = list(x for x in lista if x % 2 == 1)

if len(lista_par) > 0:
    print("\n--- Lista de N° Pares ---")
    for indice, elemento in enumerate(lista_par):
        print(f"Índice: {indice} | Elemento: {elemento}")
else:
    print("Não houveram números pares.")

if len(lista_impar) > 0:
    print("\n--- Lista de N° Ímpares ---")
    for indice, elemento in enumerate(lista_impar):
        print(f"Índice: {indice} | Elemento: {elemento}")
else:
    print("Não houveram números ímpares.")

print(f"\n• Quantidade de números pares: {len(lista_par)}")
print(f"• Quantidade de números ímpares: {len(lista_impar)}")