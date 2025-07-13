#Lista 01 - Questão 16

ca = float(input('Valor do cateto A: '))
cb = float(input('Valor do cateto B: '))

hi = (ca**2 + cb**2) ** 0.5  # Equivalente a √(ca² + cb²)

print(f'\nCateto A: {ca:.2f}')
print(f'Cateto B: {cb:.2f}')
print(f'Hipotenusa: {hi:.2f}')