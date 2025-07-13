## Lista 03 - João Paulo - Redes 1v
altura = int(input("Digite a altura do retângulo: "))
largura = int(input("Digite a largura do retângulo: "))

for i in range(altura):
    if i == 0 or i == altura - 1:
        print("* " * largura)
    else:
        print("*" + " " * (2 * (largura - 2) + 1) + "*")
