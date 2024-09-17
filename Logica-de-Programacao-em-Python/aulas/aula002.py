# Podemos obter o tipo de uma variavel usando a função type().

"""
nome = str("Ana Paula"): A string "Ana Paula" é passada para a função str(), que retorna a mesma string. A função str() é desnecessária neste caso, pois "Ana Paula" já é uma string. A variavel nome é atribuida a essa string.

idade = int(31): O inteiro 31 é passado para a função int(), que retorna o mesmo inteiro. A função int() é desnecessária neste caso, pois 31 já é um inteiro. A variavel idade é atribuida a esse inteiro.

print(type(nome)): A função type() retorna o tipo da variavel nome, que é <class 'str'>, indicando que nome é uma string. Esse valor é então impresso, resultando na saída: <class 'str'>.

"""

nome = str("Ana Paula")
idade = int(31)

print(type(nome))
print(type(idade))

# As variaveis em Python são case-sensitive, o que significa que letras maiusculas e minusculas são tratadas de forma diferente. Por exemplo, as variaveis i e I são consideradas diferentes em Python. 

i = 30
I = "Ana"

print(i)
print(I)

# Podemos tambem atribuir as variaveis em uma unica linha, separando-as por virgulas.

"""
O codigo está utilizando a desempacotamento de tuplas para atribuir varias variaveis em una unica linha e, em seguinda, imprimindo essas variaveis.

var1, var2, var3, var4 = "Texto1", "Texto2", "Texto3", "Texto4": Nesta linha, quatro strings atribuidas a quatro variaveis respectivas em uma unica operação.

A variavel var1, é atribuida à string "Texto1",
var2 é atribuida à string "Texto2",
var3 é atribuida à string "Texto3",
var4 é atribuida à string "Texto4".
"""
var1, var2, var3, var4 = "Texto1", "Texto2", "Texto3", "Texto4"

print(var1)
print(var2)
print(var3)
print(var4)

# Podemos atribuir o mesmo valor a varias variaveis em uma unica linha.
var1 = var2 = var3 = var4 = "Ana Paula"
print(var1)
print(var2)
print(var3)
print(var4)

# Se tiver uma coleção de valores em uma lista, podemos extrair em variaveis. Isso é chamado de descompactar
exemplo = "Texto 1", "Texto 2", "Texto 3", "Texto 4"
var1, var2, var3, var4 = exemplo
print(var1)
print(var2)
print(var3)
print(var4)

# A diferença a seguir é que a ','(Vírgula), separa quando o nome for uma string e junta, quando o valor do nome for um inteiro, o '+'(adição) não funciona porque uma string e um inteiro não junta. Portanto o + só funciona para textos.
nome = "Ana Paula"
print("O nome dela é", nome)
nome = 10
print("O nome dela é " + nome)


num1 = 10
num2 = 5

print(num1+num2)

# Para juntar textos e variaveis em Python usamos o caracter + ou ,

"""
Definindp duas variáveis, nome e sobrenome, que contém strings. Em seguinda, usamos a concatenação de strings para juntar essas variáveis e imprimi-las como um nome completo.

            Vamos analisar cada parte:

            nome = "Thuane": Atribui a string "Thuane" à variável nome.
            sobrenome = "Alves": Atribui a string "Alves" à variável sobrenome.

            print("Nome completo: " + nome + " " + sobrenome): Usa a concatenação de strings para juntar as variáveis nome e sobrenome, separadas por um espaço, e imprime o resultado. A saída é: Nome completo: Thuane Alves.
"""
nome = "Thuane"
sobrenome = "Alves"
print("Nome completo: " + nome + " " + sobrenome)