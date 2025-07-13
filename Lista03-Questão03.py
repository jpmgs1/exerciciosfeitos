## Lista 03 - João Paulo - Redes 1v
while True:
    numero = int(input("Digite um maior ou igual a zero: "))
    if numero >= 0:
        break
    print("Número inválido. Tente novamente.")

fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}")
