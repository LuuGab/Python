def calculadora(operacao: str, valor1, valor2) -> float:
    if not isinstance(valor1, (int, float)) or not isinstance(valor2, (int, float)):
        print("\nValor(es) Informado(s) Inválido(s).")
    else:
        if operacao.lower() == 'soma':
            return valor1+valor2
        elif operacao.lower() == 'subtração':
            return valor1-valor2
        elif operacao.lower() == 'multiplicação':
            return valor1*valor2
        elif operacao.lower() == 'divisão':
            if valor1 == 0 or valor2 == 0:
                print("\nNão é possível dividir por 0.")
            else:
                return valor1/valor2
        elif operacao.lower() == 'exponenciação':
            return valor1**valor2
        elif operacao.lower() == 'módulo':
            if valor1 == 0 or valor2 ==0:
                print("\nNão é possível dividir por 0.")
            else:
                return valor1%valor2
        else:
            print("\nOperação Aritmética inválida.")

print("--- Calculadora ---")
valor1 = float(input("- Digite o primeiro valor: "))
valor2 = float(input("- Digite o segundo valor: "))

print("\n--- Operações Aritméticas ---")
print("• Soma")
print("• Subtração")
print("• Multiplicação")
print("• Divisão")
print("• Exponenciação")
print("• Módulo")
operacao = input("- Digite a operação desejada: ")
resultado = print(f"\n• Resultado da Operação: {calculadora(operacao, valor1, valor2)}")