#João Paulo - Redes de Computadores 1v
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    maior = num1
    menor = num2
elif num2 > num1:
    maior = num2
    menor = num1
else:
    maior = menor = num1

print("\nResultado:")
print(f"→ Maior número: {maior}")
print(f"→ Menor número: {menor}")

if num1 == num2:
    print("(Os números são iguais!)")