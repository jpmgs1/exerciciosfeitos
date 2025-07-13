## Lista 04 - João Paulo - 1v - redes
tamanho = int(input("Digite o tamanho da lista: "))

numeros = []

for i in range(tamanho):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

soma = sum(numeros)
produto = 1
for num in numeros:
    produto *= num

print("Resultado:")
print(" + ".join(map(str, numeros)) + " = " + str(soma))
print(" * ".join(map(str, numeros)) + " = " + str(produto))