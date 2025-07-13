#João Paulo - Redes de Computadores 1v
def calcular_reajuste_salarial(salario):
  if salario < 500.00:
    aumento = salario * 0.30
    novo_salario = salario + aumento
    return f"Seu salário foi reajustado para R$ {novo_salario:.2f}"
  else:
    return "Não tem direito ao aumento."

salario_funcionario = float(input("Digite o seu salário: R$ "))
resultado = calcular_reajuste_salarial(salario_funcionario)
print(resultado)