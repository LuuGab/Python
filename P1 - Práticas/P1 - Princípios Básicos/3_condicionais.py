# • Estruturas Condicionais
# - if | if condição:
# - else | else:
# - elif | elif condição:

var_1 = int(input("Digite um número: "))
var_2 = int(input("Digite outro número: "))

if var_1 > var_2:
    print(f"\n{var_1} é maior que {var_2}.")
elif var_1 == var_2:
    print(f"\n{var_1} é igual a {var_2}.")
else:
    print(f"\n{var_1} é menor que {var_2}.")

if var_1 % 2 == 0:
    print(f"{var_1} é um número par.")
else:
    print(f"{var_1} é um número ímpar.")

if var2 % 2 == 0:
    print(f"{var_2} é um número par.")
else:
    print(f"{var_2} é um número ímpar.")

var_3 = float(input("\nDigite mais um número: "))

if var_3 > 0 and var_3 <= 100:
    print(f"'{var_3}' está entre 0 e 100.")
elif var_3 > 100 and var3 <=1000:
    print(f"{var_3} está entre 100 e 1000.")
else:
    pritn(f"{var_3} é maior do que 1000.")