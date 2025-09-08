lista_alunos = []
option =0

while option!=6:
    print("\n--- Lista de Alunos ---")
    print("1. Listar Alunos Registrados")
    print("2. Adicionar Novos Alunos")
    print("3. Remover Alunos")
    print("4. Substituir Alunos")
    print("5. Modificar Alunos ")
    print("6. Encerrar")
    option = int(input("Digite uma das opções acima: "))
    print(" ")

    sublista_aluno = []

    match option:
        case 1:
            if len(lista_alunos) > 0:
                for indice, alunos in enumerate(lista_alunos):
                    print(f"• Índice: {indice} | Aluno(a): {alunos[0]} | Curso: {alunos[1]} | Semestre: {alunos[2]}")
            else:
                print("• Inválido(a). Não há alunos registrados.")
        case 2:
            nome_aluno = input("• Digite o nome do aluno(a): ")
            curso_aluno = input("• Digite o curso do aluno(a): ")
            semestre_aluno = input("• Digite o semestre do aluno(a): ")

            sublista_aluno.insert(0, nome_aluno)
            sublista_aluno.insert(1, curso_aluno)
            sublista_aluno.insert(2, semestre_aluno)
            lista_alunos.append(sublista_aluno)
        case 3:
            if len(lista_alunos) > 0:
                indice_aluno = int(input("Digite o índice do aluno a ser removido(a): "))
                del lista_alunos[indice_aluno]
            else:
                print("• Inválido(a). Não há alunos registrados.")
        case 4:
            if len(lista_alunos) > 0:
                indice_aluno = int(input("Digite o índice do aluno a ser substituido: "))
                nome_aluno = input("• Digite o nome do aluno(a) substituto: ")
                curso_aluno = input("• Digite o curso do aluno(a) substituto: ")
                semestre_aluno = input("• Digite o semestre do aluno(a) substituto: ")

                sublista_aluno.insert(0, nome_aluno)
                sublista_aluno.insert(1, curso_aluno)
                sublista_aluno.insert(2, semestre_aluno)
                lista_alunos[indice_aluno] = sublista_aluno
            else:
                print("• Inválido(a). Não há alunos registrados.")
        case 5:
            print("--- Informações dos Alunos ---")
            print("1. Nome")
            print("2. Curso")
            print("3. Semestre")
            atributo_aluno = int(input("Digite o atributo do aluno a ser modificado: "))
            indice_aluno = int(input("Digite o índice do aluno a ser modificado: "))
            if atributo_aluno == 1:
                nome_aluno = input("• Insira o nome do aluno(a):")
                lista_alunos[indice_aluno].insert(0, nome_aluno)
            elif atributo_aluno == 2:
                curso_aluno = input("• Insira o curso do aluno(a):")
                lista_alunos[indice_aluno].insert(1, curso_aluno)
            elif atributo_aluno == 3:
                semestre_aluno = input("• Insira o semestre do aluno(a):")
                lista_alunos[indice_aluno].insert(2, semestre_aluno)
            else:
                print("Inválido(a).")