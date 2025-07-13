## Lista 03 - João Paulo - Redes 1v
faixa1 = faixa2 = faixa3 = faixa4 = faixa5 = 0

for i in range(1, 16):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    
    if idade <= 15:
        faixa1 += 1
    elif idade <= 30:
        faixa2 += 1
    elif idade <= 45:
        faixa3 += 1
    elif idade <= 60:
        faixa4 += 1
    else:
        faixa5 += 1

print("\nQuantidade de pessoas por faixa etária:")
print("1ª faixa (até 15 anos):", faixa1)
print("2ª faixa (16 a 30 anos):", faixa2)
print("3ª faixa (31 a 45 anos):", faixa3)
print("4ª faixa (46 a 60 anos):", faixa4)
print("5ª faixa (acima de 60 anos):", faixa5)
