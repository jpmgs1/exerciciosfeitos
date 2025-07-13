## Lista 04 - João Paulo - 1v - redes
tamanho = int(input("Digite o tamanho da lista: "))

numeros = []

for i in range(tamanho):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

ordenados = sorted(numeros)
print("\na) Lista em ordem crescente:", ordenados)

maior = max(numeros)
print("b) Maior número da lista:", maior)

menor = min(numeros)
print("c) Menor número da lista:", menor)

print("d) Elementos processados:")
for num in numeros:
    resultado = num * maior / menor
    print(f"  {num} * {maior} / {menor} = {resultado:.2f}")