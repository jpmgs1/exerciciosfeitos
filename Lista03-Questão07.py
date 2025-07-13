## Lista 03 - João Paulo - Redes 1v
precos = {1: 0.50,2: 1.00,3: 4.00,5: 7.00,9: 8.00}

total = 0.0

while True:
    codigo = int(input("Digite o código do produto (ou 0 para encerrar): "))
    
    if codigo == 0:
        break

    if codigo not in precos:
        print("Código Inválido.")
        continue

    quantidade = int(input("Digite a quantidade comprada: "))
    total += precos[codigo] * quantidade

print(f"\nTotal da compra: R$ {total:.2f}")
