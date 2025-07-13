#Lista 01 - Questão 20

n = int(input("Digite o número de lados do polígono: "))

diagonais = n * (n - 3) // 2
print(f"Um polígono de {n} lados tem {diagonais} diagonais")