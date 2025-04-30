#Lista 01 - Questão 07

salario_fixo = float(input("Digite o salário fixo do funcionário: R$ "))
vendas = float(input("Digite o valor total de vendas do funcionário: R$ "))

comissao = vendas * 0.04

salario_final = salario_fixo + comissao

print(f"Comissão sobre vendas: R$ {comissao:.2f}")
print(f"Salário final do funcionário: R$ {salario_final:.2f}")

