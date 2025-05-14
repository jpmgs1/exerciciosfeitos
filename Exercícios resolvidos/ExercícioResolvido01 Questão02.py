n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
faltas = int(input("Digite o número de faltas: "))

n1_valida = 0 <= n1 <= 10
n2_valida = 0 <= n2 <= 10
n3_valida = 0 <= n3 <= 10
n4_valida = 0 <= n4 <= 10
faltas_validas = 0 <= faltas <= 60

if n1_valida and n2_valida and n3_valida and n4_valida:
    media = (2*n1 + 2*n2 + 3*n3 + 3*n4) / 10
else:
    media = None

reprovado_faltas = faltas > 20 if faltas_validas else False
reprovado_media = (media is not None) and (media < 3) and not reprovado_faltas
recuperacao = (media is not None) and (3 <= media < 7) and not reprovado_faltas
aprovado = (media is not None) and (7 <= media <= 10) and not reprovado_faltas

if media is not None:
    print(f"\nMédia final: {media:.2f}")
else:
    print("\nNão foi possível calcular a média por causa de nota(s) inválida(s).")

print("\nSituações:")
print(f"A primeira nota digitada é válida? {n1_valida}")
print(f"A segunda nota digitada é válida? {n2_valida}")
print(f"A terceira nota digitada é válida? {n3_valida}")
print(f"A quarta nota digitada é válida? {n4_valida}")
print(f"O número de faltas digitado é válido? {faltas_validas}")
print(f"O aluno está reprovado por faltas? {reprovado_faltas}")
print(f"O aluno está reprovado por média? {reprovado_media}")
print(f"O aluno está em recuperação? {recuperacao}")
print(f"O aluno está aprovado? {aprovado}")
