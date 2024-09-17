# Aula Input

nome = input("Digite seu nome: \n")

print("O seu nome é:", nome)

"""
Solicita ao usuário que insira seu nome e duas notas, calcula a média dessas notas e, em seguida, imprime uma mensagem contendo o nome do aluno e a média calculada.

        Vamos analisar cada parte do código:

        nome = input("Digite seu nome: \n"): Solicita ao usuário que digite seu nome e armazena o valor digitado na variável nome.

        nota1 = float(input("Digite a primeira nota: \n")): Solicita ao usuário que digite a primeira nota e armazena o valor digitado na variável nota1. A função float() é utilizada para converter o valor digitado para um número decimal.

        nota2 = float(input("Digite a segunda nota: \n")): Solicita ao usuário que digite a segunda nota e armazena o valor digitado na variável nota2. Assim como no caso anterior, a função float() é utilizada para converter o valor digitado para um número decimal.

        media = (nota1 + nota2) / 2: Calcula a média das duas notas digitadas pelo usuário, e dividindo a soma pelo número de notas (2). A média é armazenada na variável media.

        print(f"A média do aluno {nome} é: {media:.2f}"): Imprime uma mensagem contendo o nome do aluno e a média calculada, formatando a média para exibir apenas duas casas decimais.

        O resultado final combina os valores das variáveis nome e media com as strings literais para exibir a mensagem formatada na tela.
"""
nome = input("Digite seu nome: \n")
nota1 = float(input("Digite a primeira nota: \n"))
nota2 = float(input("Digite a segunda nota: \n"))

media = (nota1 + nota2) / 2

print(f"A média do aluno {nome} é: {media:.2f}")