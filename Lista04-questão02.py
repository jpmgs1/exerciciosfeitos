## Lista 04 - João Paulo - 1v - redes
alunos = []
print("Cadastro de Alunos (digite 'sair' no nome para encerrar)\n")

while True:
    nome = input("Nome do aluno: ").strip()
    
    if nome.lower() == 'sair':
        break
    
    while True:
        try:
            media = float(input("Média do aluno (0-10): "))
            if 0 <= media <= 10:
                break
            else:
                print("A média deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Valor inválido! Digite um número entre 0 e 10.")
    
    if media >= 6:
        situacao = "Aprovado"
    elif media < 2:
        situacao = "Reprovado"
    else:
        situacao = "Recuperação"
    
    alunos.append({
        'nome': nome,
        'media': media,
        'situacao': situacao
    })

print("\nSituação dos Alunos:")
for aluno in alunos:
    print(f"{aluno['nome']} - Média: {aluno['media']:.1f} - {aluno['situacao']}")