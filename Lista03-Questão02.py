## Lista 03 - João Paulo - Redes 1v
inicio = int(input("Digite o valor inicial da tabuada: "))
fim = int(input("Digite o valor final da tabuada: "))

for i in range(1, 10):
    print(f"\nTabuada do {i}:")
    for j in range(inicio, fim + 1):
        soma = i + j
        produto = i * j
        print(f"{i} + {j} = {soma:2} | {i} x {j} = {produto:2}")
