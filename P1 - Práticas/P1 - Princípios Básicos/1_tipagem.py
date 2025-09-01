# Python é uma linguagem de tipagem dinâmica, ou seja, não é necessário declarar o tipo da variável.

# • Tipos de Variáveis:
# - String | str
# - Inteiro | int
# - Float | float
# - Booleano | bool

var_1 = "7"
var_2 = 7
var_3 = 7.0
var_4 = True

# • Função Input | Entrada de Dados
var_5 = input("Digite um valor para var5: ")
var_6 = input("Digite um valor para var6: ")

# • Observação | É importante saber que a função input sempre atribui um valor string a variável em questão. Sendo necessário fazer o casting para ter o tipo desejado. 

# • Casting | Mudar o tipo do valor, ou da própria variável
print(f"\nTipo da Variável: {type(var_5)}")
print(f"Casting...")
var5 = int(var_5)
print(f"Tipo da Variável: {type(var_5)}")
print("")

