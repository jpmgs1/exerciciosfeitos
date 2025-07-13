## Lista 04 - João Paulo - 1v - redes
tamanho = int(input("Quantos números você quer inserir? "))
numeros = []

for i in range(tamanho):
    valor = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(valor)

divisiveis_por_2 = []
divisiveis_por_3 = []
divisiveis_por_2_e_3 = []

for num in numeros:
    if num % 2 == 0:
        divisiveis_por_2.append(num)
    if num % 3 == 0:
        divisiveis_por_3.append(num)
    if num % 2 == 0 and num % 3 == 0:
        divisiveis_por_2_e_3.append(num)

print("\nNúmeros divisíveis por 2:", divisiveis_por_2)
print("Números divisíveis por 3:", divisiveis_por_3)
print("Números divisíveis por 2 e por 3:", divisiveis_por_2_e_3)
