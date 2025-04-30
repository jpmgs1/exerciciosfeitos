#Lista 01 - Questão 13

salario_minimo = float(input("Digite o valor do salário-mínimo: "))
salario_funcionario = float(input("Digite o valor do salário do funcionário: "))

quantidade = salario_funcionario // salario_minimo

print("O funcionário recebe", int(quantidade), "salário(s)-mínimo(s) completo(s).")