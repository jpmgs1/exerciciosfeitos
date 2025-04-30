#Lista 01 - Questão 19

largura = float(input("Digite a largura do cômodo (em metros): "))
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

area = largura * comprimento
potencia = area * 18  # 18 W por m²

print(f"\nÁrea do cômodo: {area:.2f} m²")
print(f"Potência de iluminação necessária: {potencia:.2f} Watts")