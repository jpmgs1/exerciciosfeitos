#João Paulo - Redes de Computadores 1v
def calcular_reajuste_salarial(salario):
  if salario <= 300.00:
    percentual_aumento = 0.35  # 35%
  else:
    percentual_aumento = 0.15  # 15%

  aumento = salario * percentual_aumento
  novo_salario = salario + aumento
  return f"O salário reajustado é de R$ {novo_salario:.2f}"

salario_funcionario = float(input("Digite o seu salário: R$ "))
resultado = calcular_reajuste_salarial(salario_funcionario)
print(resultado)