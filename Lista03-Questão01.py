## Lista 03 - João Paulo - Redes 1v
soma = 0
quantidade = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    soma += numero
    quantidade += 1
if quantidade > 0:
    media = soma / quantidade
    print("Números digitados:", quantidade)
    print("Soma dos números:", soma)
    print("Média dos números:", media)
else:
    print("Nenhum número foi digitado.")
