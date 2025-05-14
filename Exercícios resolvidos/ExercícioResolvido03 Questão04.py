valor_casa = float(input("Digite o valor da casa a comprar: R$ "))
salario = float(input("Digite o seu salário mensal: R$ "))
anos_pagar = int(input("Digite em quantos anos você deseja pagar: "))

meses_pagar = anos_pagar * 12
prestacao_mensal = valor_casa / meses_pagar
limite_prestacao = salario * 0.30

print(f"\nValor da casa: R$ {valor_casa:.2f}")
print(f"Salário mensal: R$ {salario:.2f}")
print(f"Prazo para pagamento: {anos_pagar} anos ({meses_pagar} meses)")
print(f"Valor da prestação mensal: R$ {prestacao_mensal:.2f}")
print(f"Limite máximo da prestação (30% do salário): R$ {limite_prestacao:.2f}")

if prestacao_mensal <= limite_prestacao:
  print("\nEmpréstimo APROVADO!")
else:
  print("\nEmpréstimo REPROVADO.")
  print("O valor da prestação mensal excede 30% do seu salário.")