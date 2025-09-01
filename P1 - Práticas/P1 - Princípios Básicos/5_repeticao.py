# For | Estrutura utilizada para repetir o bloco do código determinada quantidade de vezes específicada na função range().
lista_alunos = []
continuar = True

while continuar!=False:
    resp = input(("\nDeseja fazer o lançamento de notas de alunos? (S/N): "))
    if resp.upper() == "S":
        quantidade = int(input("Digite a quantidade de notas: "))
        if quantidade > 0:
            for i in range(quantidade):
                nome_aluno = input(("\nNome do Aluno(a): "))
                nota_aluno = float(input(("Nota do Aluno(a): ")))
                lista_alunos.append(([nome_aluno, nota_aluno]))
        elif quantidade == 0:
            print("Encerrando...")
            continuar = False
        else:
            print("Valor Inválido.")
    elif resp.upper() == "N":
        print("Encerrando...")
        continuar = False
    else:
        print("Resposta Inválida.")

if len(lista_alunos)!=0:
    print("\nLista de Alunos:")
    for aluno in lista_alunos:
        print(f"• Aluno(a): {aluno[0]} | Nota: {aluno[1]}")
else:
    print("\nNão há nenhum aluno(a).")