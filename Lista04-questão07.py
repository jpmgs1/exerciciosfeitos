## Lista 04 - João Paulo - 1v - redes
quantidade_alunos = int(input("Quantos alunos deseja cadastrar? "))
alunos = []

for i in range(quantidade_alunos):
    print(f"\nAluno {i+1}:")
    nome = input("Nome: ")
    notas = []
    for j in range(4):
        nota = float(input(f"Nota {j+1}: "))
        notas.append(nota)
    
    media = sum(notas) / 4
    
    if media >= 7:
        situacao = "Aprovado"
    elif media < 3:
        situacao = "Reprovado"
    else:
        situacao = "Recuperação"
    
    alunos.append({
        'nome': nome,
        'notas': notas,
        'media': media,
        'situacao': situacao
    })

print("\na) Relação completa de alunos:")
for aluno in alunos:
    print(f"\nNome: {aluno['nome']}")
    print(f"Notas: {', '.join(map(str, aluno['notas']))}")
    print(f"Média: {aluno['media']:.1f}")
    print(f"Situação: {aluno['situacao']}")

print("\nb) Alunos aprovados:")
aprovados = [aluno['nome'] for aluno in alunos if aluno['situacao'] == "Aprovado"]
print('\n'.join(aprovados) if aprovados else "Nenhum aluno aprovado")

print("\nc) Alunos em recuperação:")
recuperacao = [aluno['nome'] for aluno in alunos if aluno['situacao'] == "Recuperação"]
print('\n'.join(recuperacao) if recuperacao else "Nenhum aluno em recuperação")

print("\nd) Alunos reprovados:")
reprovados = [aluno['nome'] for aluno in alunos if aluno['situacao'] == "Reprovado"]
print('\n'.join(reprovados) if reprovados else "Nenhum aluno reprovado")