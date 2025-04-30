#Lista 01 - Questão 10

base_maior = float(input("Digite o valor da base maior (em cm): "))
base_menor = float(input("Digite o valor da base menor (em cm): "))
altura = float(input("Digite o valor da altura (em cm): "))

area = (base_maior + base_menor) * altura / 2

print(f"A área do trapézio é: {area} cm²")

