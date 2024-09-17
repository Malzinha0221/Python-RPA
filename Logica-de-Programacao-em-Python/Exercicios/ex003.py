"""
    Exercício: Tabuada Personalizada

"""

num = int(input("Digite um número: "))

print(f"Tabuada do {num}")
for i in range(0, 11):
    print(f"{num} x {i} = {num*i}")


# Outra forma de responder essa atividade

# Tabuada 

nDigitado = int(input("A tabuada de qual número você deseja ver? "))

print(f"Tabuada do {nDigitado}")

print(nDigitado, "x 0 =", nDigitado * 0)
print(nDigitado, "x 1 =", nDigitado * 1)
print(nDigitado, "x 2 =", nDigitado * 2)
print(nDigitado, "x 3 =", nDigitado * 3)
print(nDigitado, "x 4 =", nDigitado * 4)
print(nDigitado, "x 5 =", nDigitado * 5)
print(nDigitado, "x 6 =", nDigitado * 6)
print(nDigitado, "x 7 =", nDigitado * 7)
print(nDigitado, "x 8 =", nDigitado * 8)
print(nDigitado, "x 9 =", nDigitado * 9)
print(nDigitado, "x 10 =", nDigitado * 10)