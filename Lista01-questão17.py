#Lista 01 - Questão 17

import math
raio = float(input("Digite o raio da circunferência: "))

comprimento = 2 * math.pi * raio
area = math.pi * raio ** 2
volume = (4/3) * math.pi * raio ** 3

print(f"\nResultados para raio = {raio:.2f}:")
#a)
print(f"Comprimento = {comprimento:.2f}")
#b)
print(f"Área = {area:.2f}")
#c)
print(f"Volume da esfera = {volume:.2f}")