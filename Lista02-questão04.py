#João Paulo - Redes de Computadores 1v
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print(f"\n→ Maior número: {maior}")
print(f"→ Menor número: {menor}")

if num1 == num2 == num3:
    print("(Todos os números são iguais!)")