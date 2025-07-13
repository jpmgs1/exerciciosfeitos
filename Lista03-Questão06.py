## Lista 03 - João Paulo - Redes 1v
vista_total = prazo_total = total_geral = 0
menor = float('inf')
maior = float('-inf')

for i in range(1, 16):
    print(f"\nTransação {i}:")
    while True:
        codigo = input("Digite o código da transação (V para à vista, P para a prazo): ").strip().upper()
        if codigo in ['V', 'P']:
            break
        print("Código inválido. Digite apenas V ou P.")
    
    valor = float(input("Digite o valor da transação: "))
    
    if codigo == 'V':
        vista_total += valor
    else:
        prazo_total += valor

    total_geral += valor

    if valor < menor:
        menor = valor
    if valor > maior:
        maior = valor

print("\n=== Relatório de Transações ===")
print(f"Total das compras à vista : R$ {vista_total:.2f}")
print(f"Total das compras a prazo : R$ {prazo_total:.2f}")
print(f"Total geral das compras   : R$ {total_geral:.2f}")
print(f"Menor valor de compra     : R$ {menor:.2f}")
print(f"Maior valor de compra     : R$ {maior:.2f}")
