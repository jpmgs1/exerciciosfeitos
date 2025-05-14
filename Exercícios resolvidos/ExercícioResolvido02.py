n1 = float(input("Nota 1 (0 a 10): "))
n2 = float(input("Nota 2 (0 a 10): "))
n3 = float(input("Nota 3 (0 a 10): "))
n4 = float(input("Nota 4 (0 a 10): "))
faltas = int(input("Número de faltas (0 a 60): "))

if not (0 <= n1 <= 10 and 0 <= n2 <= 10 and 0 <= n3 <= 10 and 0 <= n4 <= 10):
    print("Erro: Todas as notas devem estar entre 0 e 10.")
elif not (0 <= faltas <= 60):
    print("Erro: O número de faltas deve estar entre 0 e 60.")
else:
    media = (2*n1 + 2*n2 + 3*n3 + 3*n4) / 10
    print(f"Média: {media:.2f}")

    if faltas > 20:
        print("Situação: Reprovado por faltas")
    elif media >= 9:
        print("Situação: Aprovado com louvor")
    elif media >= 7:
        print("Situação: Aprovado")
    elif media >= 3:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado por média")
