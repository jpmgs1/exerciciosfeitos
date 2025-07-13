## Lista 04 - João Paulo - 1v - redes
tamanho = int(input("Quantos números você deseja digitar? "))
numeros = []
for i in range(tamanho):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

frequencia = {}
for numero in numeros:
    if numero in frequencia:
        frequencia[numero] += 1
    else:
        frequencia[numero] = 1

print("\nFrequência dos números:")
for numero in sorted(frequencia):
    vezes = frequencia[numero]
    print(f"* {numero} aparece {vezes} vez{'es' if vezes > 1 else ''}")