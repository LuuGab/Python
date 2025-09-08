nome_completo = input("\n• Digite seu nome: ")
num_protocolo = input("• Digite o n° do protocolo: ")
data_protocolo = input("• Digite a data do protocolo (DD/MM/AAAA): ")

ultimo_nome = nome_completo.split()[-1]
ultimo_ano = data_protocolo.split("/")[-1]
validade = str(2025 - int(data_protocolo.split("/")[-1]))

nome_split = nome_completo.split()
lista_letra = []

for elemento in nome_split:
    ultimo_caractere = elemento[-1]
    lista_letra.append(ultimo_caractere)

join_letra = "".join(lista_letra)
identificador = num_protocolo+"-"+join_letra+"-" +ultimo_ano

print(f"\n• Sr(a). {ultimo_nome}, o seu identificador é: {identificador}.")
print(f"• Seu protocolo irá perder a validade em {validade} anos!")