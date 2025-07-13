#João Paulo - Redes de Computadores 1v
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"\nMédia do aluno: {media:.1f}")

if media >= 0 and media < 4.0:
    mensagem = "Reprovado"
elif media >= 4.0 and media < 7.0:
    mensagem = "Prova Final"
elif media >= 7.0 and media <= 10.0:
    mensagem = "Aprovado"
else:
    mensagem = "Digite notas válidas (Digite Nota de 0 a 10)"

print(f"Erro na Digitação: {mensagem}")