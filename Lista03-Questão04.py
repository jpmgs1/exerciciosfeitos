## Lista 03 - João Paulo - Redes 1v
n = int(input("Digite quantos números da sequência de Fibonacci deseja ver: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
