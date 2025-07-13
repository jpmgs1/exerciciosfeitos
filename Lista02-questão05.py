# Calculadora Simples - João Paulo
print("Calculadora Simples")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("\nOpções:")
print("1 - Média")
print("2 - Diferença (maior - menor)")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potência (n1 elevado a n2)")
print("6 - Raiz Quadrada")
print("7 - Raiz Cúbica")
op = input("Escolha uma opção (1-7): ")

if op == '1':
    print(f"\nMédia: {(n1+n2)/2:.2f}")
elif op == '2':
    print(f"\nDiferença: {max(n1,n2)-min(n1,n2):.2f}")
elif op == '3':
    print(f"\nMultiplicação: {n1*n2:.2f}")
elif op == '4':
    if n2 == 0:
        print("\nErro: Não pode dividir por zero!")
    else:
        print(f"\nDivisão: {n1/n2:.2f}")
elif op == '5':
    print(f"\nPotência: {n1**n2:.2f}")
elif op == '6':
    if n1 >= 0:
        print(f"\nRaiz quadrada de {n1}: {n1**0.5:.2f}")
    else:
        print(f"\nRaiz quadrada de {n1}: Não existe (negativo)")
    if n2 >= 0:
        print(f"Raiz quadrada de {n2}: {n2**0.5:.2f}")
    else:
        print(f"Raiz quadrada de {n2}: Não existe (negativo)")
elif op == '7':
    print(f"\nRaiz cúbica de {n1}: {n1**(1/3):.2f}")
    print(f"Raiz cúbica de {n2}: {n2**(1/3):.2f}")
else:
    print("\nOpção inválida!")