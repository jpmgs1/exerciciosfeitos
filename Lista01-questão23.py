#Lista 01 - Questão 23

valor = int(input("Digite o valor do saque: "))

notas_100 = valor // 100
resto = valor % 100

notas_50 = resto // 50
resto = resto % 50

notas_20 = resto // 20
resto = resto % 20

notas_10 = resto // 10
resto = resto % 10

notas_5 = resto // 5

print("\n* Resultado *")
print(f"Notas de 100: {notas_100}")
print(f"Notas de 50: {notas_50}")
print(f"Notas de 20: {notas_20}")
print(f"Notas de 10: {notas_10}")
print(f"Notas de 5: {notas_5}")