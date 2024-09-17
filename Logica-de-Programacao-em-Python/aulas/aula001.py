# Este sinal serve para comentar um código para que o usuario saiba o que codigo faz

"""
Usando 3 aspas podemos
comentar varias linhas
assim quando o codigo for executado o script pula essas linhas
"""

print("Script execultado com sucesso!")
print("Olá Mundo!")

# Para que serve uma variavel?
"""
O que é uma variavel?

Uma variável é um nome que se refere a um valor armazenado na memória do computador. Em programação, as variaveis são usadas para armazenar dados que podem ser alterados durante a execução de um programa.

Em Python, as variaveis não são declaradas com um tipo específico. No entanto, os tipos de dados que voce pode armazenar em uma variavel inclue:
"""

# Principais tipos de variaveis

# Inteiros (int): Numeros inteiros, positivos ou negativos, sem casas decimais.
inteiro = 10
print("Inteiro:", inteiro)

# Ponto flutuante (float): Numeros Reiais, que tem parte decimais.
flutuante = 10.5
print("Flutuante:", flutuante)

#Complexos (complex): Numeros complexos, com uma parte real e uma parte imaginaria.
complexo = 3 + 4j
print("Complexo:", complexo)

# String (str): Sequencia de caracteres, como letras, digitos e simbolos.
texto = "Olá Mundo!"
print("Texto:", texto)

"""
Os termos "mutavel" e "imutavel" referem-se à capacidade de alterar o conteúdo de um objeto depois que ele foi criado.

Mutável: Significa que o conteúdo do objeto pode ser alterado após a criação. As listas Python são mutáveis, o que significa que você pode modificar seus elementos.

Imutável: Significa que o conteúdo do objeto não pode ser alterado após a sua criação. As tuplas em Python são imutáveis, o que significa que, uma vez criada, voce não pode modificar seus elementos.
"""
# Listas (list): Uma coleção ordenada e mutável de valores.
listas = [1, 2, 3, 4, 5]
print("Lista:", listas)

# Tuplas (tuple): Uma coleção ordenada e imutável de valores.

tuplas = (1, 2, 3, 4, 5)
print("Tupla:", tuplas)

# Conjuntos (set): Uma coleção não ordenada e mutável de valores únicos.
conjuntos = {1, 2, 3, 4, 3, 5}
print("Conjunto:", conjuntos)

#Dicionarios (dict): Uma coleção não ordenada de chave-valor.
dicionarios = {"nome": "João", "idade": 30}
print("Dicionario:", dicionarios)

# Booleanos (bool): Valores verdadeiro ou falso.

verdadeiro = True
falso = False
print("Booleanos:", verdadeiro, falso)

# None: Um valor especial que representa a ausência de um valor.

nenhum = None
print("Nenhum:", nenhum)

# Exemplo de variaveis

# Variaveis 

idade = 30
nome = "João"

print("Nome:", nome)
print("Idade:", idade)