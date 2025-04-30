#Lista 01 - Questão 14

numero = int(input("Digite um número inteiro: "))

print(f"\nTabuada de adição do {numero}:")
for i in range(0, 11):
    print(f"{numero} + {i} = {numero + i}")

print(f"\nTabuada de multiplicação do {numero}:")
for i in range(0, 11):
    print(f"{numero} x {i} = {numero * i}")